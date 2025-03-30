#!/usr/bin/env python3

import os
import re
import json
import yaml
import frontmatter
import requests
import datetime
import subprocess
import logging
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Set

# Configure logging
log_level = logging.DEBUG if os.environ.get("DEBUG") == "1" else logging.INFO
logging.basicConfig(
    level=log_level,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logging.info(f"Logging level set to: {logging.getLevelName(log_level)}")

# Configuration
BUTTONDOWN_API_KEY = os.environ.get("BUTTONDOWN_API_KEY")
BUTTONDOWN_TAGS = os.environ.get("BUTTONDOWN_TAGS", "").split(",")
BUTTONDOWN_API_URL = "https://api.buttondown.email/v1"
CONTENT_DIR = Path(os.getcwd()) / "content"  # Use content subdirectory within current working directory


# Tag colors to use for created tags (will cycle through these)
TAG_COLORS = [
    "#FF5733",  # Red
    "#33FF57",  # Green
    "#3357FF",  # Blue
    "#FF33A8",  # Pink
    "#33FFF5",  # Cyan
    "#FFD700",  # Gold
    "#A033FF",  # Purple
    "#FF8C33",  # Orange
    "#33FFBD",  # Mint
    "#8CFF33"   # Lime
]

def run_command(cmd: List[str]) -> str:
    """Run a shell command and return its output"""
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        return result.stdout.strip()

    print(f"Error running command: {' '.join(cmd)}")
    print(f"Error: {result.stderr}")
    raise RuntimeError(f"Command failed: {' '.join(cmd)}")

def get_content_files() -> List[Path]:
    """Get all content files in the content directory"""
    logging.debug(f"Looking for content files in: {CONTENT_DIR}")

    files = []
    for ext in [".md", ".markdown"]:
        pattern = f"**/*{ext}"
        matched_files = list(CONTENT_DIR.glob(pattern))
        files.extend(matched_files)

    return files

def is_eligible(post: frontmatter.Post, start_date: datetime.date) -> bool:
    """Check if a post is eligible for Buttondown integration"""
    title = post.get('title', 'Untitled Post')

    # Skip if already published in Buttondown
    buttondown_data = post.get("buttondown", {})
    if isinstance(buttondown_data, dict) and buttondown_data.get("published"):
        logging.debug(f"Post '{title}' already published in Buttondown, skipping")
        return False

    # Check if the post has any of the tags in BUTTONDOWN_TAGS
    # In Hugo, the tags are under the "categories" key
    post_tags = post.get("categories", [])
    if not any(tag in BUTTONDOWN_TAGS for tag in post_tags):
        return False

    # Check if the post has a date
    post_date = post.get("date")
    if not post_date:
        return False

    # Convert post_date to datetime.date if it's a datetime
    if isinstance(post_date, datetime.datetime):
        post_date = post_date.date()

    # Check if the post was created after start_date
    is_eligible = post_date > start_date
    return is_eligible

def is_published(post: frontmatter.Post) -> bool:
    """Check if a post is published in Hugo"""
    draft = post.get("draft", False)
    return not draft

def get_buttondown_email(email_id: str) -> Dict:
    """Get a Buttondown email by ID"""
    headers = get_api_headers()
    response = requests.get(f"{BUTTONDOWN_API_URL}/emails/{email_id}", headers=headers)

    if response.status_code != 200:
        print(f"Error getting Buttondown email: {response.status_code}")
        print(f"Response: {response.text}")
        response.raise_for_status()

    return response.json()

def get_api_headers() -> Dict[str, str]:
    """Create API headers for Buttondown requests."""
    return {
        "Authorization": f"Token {BUTTONDOWN_API_KEY}",
        "Content-Type": "application/json"
    }


def prepare_email_data(post: frontmatter.Post, is_draft: bool) -> Dict:
    """Prepare common data for Buttondown email creation/update."""
    # Extract eligible tags from the categories field
    post_categories = post.get("categories", [])
    eligible_tags = [tag for tag in post_categories if tag in BUTTONDOWN_TAGS]

    title = post.get("title", "Untitled Post")
    logging.debug(f"Preparing email data for post '{title}'")
    logging.debug(f"Eligible tags from categories: {eligible_tags}")

    data = {
        "subject": title,
        "body": post.content,
        "status": "draft" if is_draft else "scheduled",
    }

    # Add filters for subscriber metadata
    filter_objects = [
        {
            "field": f"subscriber.metadata.all_email",
            "operator": "equals",
            "value": "1"
        }
    ]
    filter_objects.extend(
        {
            "field": f"subscriber.metadata.{tag_name}",
            "operator": "equals",
            "value": "1"
        }
        for tag_name in eligible_tags
    )

    data["filters"] = {
        "predicate": "or",  # Use OR to send to subscribers with any of the matching tags
        "filters": filter_objects,
        "groups": []
    }
    logging.debug(f"Added filters with tag names: {eligible_tags}")
    logging.debug(f"Filter objects: {filter_objects}")

    # Set publish date for non-draft emails
    if not is_draft:
        now = datetime.datetime.now().astimezone() + datetime.timedelta(seconds=10)
        data["publish_date"] = now.isoformat()

    return data

def create_buttondown_email(post: frontmatter.Post, is_draft: bool) -> str:
    """Create a new Buttondown email"""
    title = post.get("title", "Untitled Post")
    status = "draft" if is_draft else "published"
    logging.info(f"Creating new {status} Buttondown email for: {title}")

    headers = get_api_headers()
    data = prepare_email_data(post, is_draft)
    response = requests.post(f"{BUTTONDOWN_API_URL}/emails", headers=headers, json=data)

    # Check for successful response
    if response.status_code in (200, 201):
        email_data = response.json()
        logging.info(f"Successfully created email with ID: {email_data['id']}")
        return email_data["id"]

    # Handle error case
    logging.error(f"Error creating Buttondown email: {response.status_code}")
    logging.error(f"Response: {response.text}")
    response.raise_for_status()

def update_buttondown_email(email_id: str, post: frontmatter.Post, is_draft: bool) -> None:
    """Update an existing Buttondown email"""
    title = post.get("title", "Untitled Post")
    status = "draft" if is_draft else "published"
    logging.info(f"Updating {status} Buttondown email {email_id} for: {title}")

    headers = get_api_headers()
    data = prepare_email_data(post, is_draft)
    response = requests.patch(f"{BUTTONDOWN_API_URL}/emails/{email_id}", headers=headers, json=data)

    # Return early if successful
    if response.status_code == 200:
        logging.info(f"Successfully updated email {email_id}")
        return

    # Handle error case
    logging.error(f"Error updating Buttondown email: {response.status_code}")
    logging.error(f"Response: {response.text}")
    response.raise_for_status()

def send_draft_email(email_id: str, subscriber_id: str) -> None:
    """Send a draft email to a specific subscriber"""
    logging.info(f"Sending test email for {email_id} to subscriber: {subscriber_id}")
    headers = get_api_headers()

    data = {
        "subscribers": [
            subscriber_id
        ]
    }

    response = requests.post(f"{BUTTONDOWN_API_URL}/emails/{email_id}/send-draft", headers=headers, json=data)

    # Return early if successful
    if response.status_code == 200:
        logging.info(f"Successfully sent test email for {email_id}")
        return

    # Handle error case
    logging.error(f"Error sending draft email: {response.status_code}")
    logging.error(f"Response: {response.text}")
    response.raise_for_status()

def update_post_frontmatter(file_path: Path, email_id: str, sent: bool, commit_message: str) -> None:
    """Update post frontmatter with Buttondown email ID and commit changes"""
    logging.info(f"Updating frontmatter for {file_path.name} with email ID: {email_id}")
    post = frontmatter.load(file_path)

    # Update buttondown data in frontmatter
    buttondown_data = post.get("buttondown", {})
    if not isinstance(buttondown_data, dict):
        buttondown_data = {}

    buttondown_data["id"] = email_id
    if sent:
        buttondown_data["sent"] = True
    post["buttondown"] = buttondown_data

    # Write updated frontmatter back to file
    with open(file_path, "w") as f:
        f.write(frontmatter.dumps(post, sort_keys=False))
    logging.info(f"Wrote updated frontmatter to {file_path}")

    # Commit changes
    logging.info(f"Committing changes with message: {commit_message}")
    run_command(["git", "add", str(file_path)])
    run_command(["git", "commit", "-m", commit_message])
    logging.info(f"Committed changes successfully")

def handle_published_post(file_path: Path, post: frontmatter.Post, existing_email_id: Optional[str]) -> None:
    """Handle published post processing logic."""
    title = post.get("title", "Untitled Post")

    # Simple case, create and send straight away if no previous drafts.
    if not existing_email_id:
        logging.info(f"Creating new Buttondown email for published post: {title}")
        email_id = create_buttondown_email(post, False)
        logging.info(f"Created email with ID: {email_id}")

        update_post_frontmatter(
            file_path,
            email_id,
            True,
            f"Created and sent Buttondown email for {file_path.name}"
        )
        logging.info(f"Updated frontmatter with email ID")
        return

    logging.info(f"Checking status of existing email ID: {existing_email_id}")
    email_data = get_buttondown_email(existing_email_id)

    msg = "Updated state"
    if email_data.get("status") != "sent":
        logging.info(f"Updating existing draft email to published state: {existing_email_id}")
        update_buttondown_email(existing_email_id, post, False)
        msg = f"Updated existing draft and sent Buttondown email for {file_path.name}"
    else:
        logging.info(f"Email for {title} already sent in buttondown, updating frontmatter.")
        msg = f"Marked {file_path.name} as already sent in Buttondown"

    update_post_frontmatter(
        file_path,
        existing_email_id,
        True,
        msg
    )
    return

def handle_draft_post(file_path: Path, post: frontmatter.Post, existing_email_id: Optional[str], test_subscriber_id: str) -> None:
    """Handle draft post processing logic."""
    title = post.get("title", "Untitled Post")
    email_id = existing_email_id

    if existing_email_id:
        logging.info(f"Updating existing draft email: {existing_email_id} for {title}")
        update_buttondown_email(existing_email_id, post, True)
        logging.info("Updated draft email")
    else:
        logging.info(f"Creating new draft email for: {title}")
        email_id = create_buttondown_email(post, True)
        update_post_frontmatter(
            file_path,
            email_id,
            False,
            f"Created draft Buttondown email for {file_path.name}"
        )

    # Send test email if a subscriber ID is provided
    if test_subscriber_id and email_id:
        logging.info(f"Sending test email to subscriber ID: {test_subscriber_id}")
        send_draft_email(email_id, test_subscriber_id)

def get_existing_email_id(post: frontmatter.Post) -> Optional[str]:
    """Extract Buttondown email ID from post frontmatter."""
    buttondown_data = post.get("buttondown", {})
    if not isinstance(buttondown_data, dict):
        return None
    return buttondown_data.get("id")

def process_post(file_path: Path, start_date: datetime.date, test_subscriber_id: str) -> None:
    """Process a single post."""
    post = frontmatter.load(file_path)
    title = post.get("title", "Untitled Post")

    # Skip non-eligible posts
    if not is_eligible(post, start_date):
        return

    published = is_published(post)
    existing_email_id = get_existing_email_id(post)

    if post.get("buttondown", {}).get("sent", False):
        logging.info(f"Post {title} ({file_path.name}) is marked as sent, skipping")
    elif published:
        logging.info(f"Post {title} ({file_path.name}) is published, handling as published post")
        handle_published_post(file_path, post, existing_email_id)
    else:
        logging.info(f"Post {title} ({file_path.name}) is a draft, handling as draft post")
        handle_draft_post(file_path, post, existing_email_id, test_subscriber_id)

def validate_configuration() -> None:
    """Validate required environment variables."""
    if not BUTTONDOWN_API_KEY:
        raise ValueError("BUTTONDOWN_API_KEY environment variable is required")

    if not BUTTONDOWN_TAGS:
        raise ValueError("BUTTONDOWN_TAGS environment variable is required")

def main():
    """Main function to sync Hugo posts with Buttondown"""
    logging.info("Starting Buttondown sync process")

    # Ignore posts before the date buttondown was adopted.
    start_date = datetime.date(2025, 3, 29)
    logging.info(f"Using start date: {start_date}")

    # Validate configuration
    validate_configuration()
    logging.info("Configuration validated")

    # Get test subscriber ID from environment
    test_subscriber_id = os.environ.get("BUTTONDOWN_TEST_SUBSCRIBER_ID", "")
    if test_subscriber_id:
        logging.info("Test subscriber ID is configured")

    # Process each content file
    content_files = get_content_files()
    logging.info(f"Found {len(content_files)} content files to process")

    processed_count = 0
    for file_path in content_files:
        try:
            process_post(file_path, start_date, test_subscriber_id)
            processed_count += 1
        except Exception as e:
            logging.error(f"Error processing {file_path}: {e}")
            continue

    logging.info(f"Buttondown sync complete. Processed {processed_count} eligible posts.")

if __name__ == "__main__":
    main()