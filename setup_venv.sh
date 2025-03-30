#!/bin/bash
set -e

# Script to set up a virtual environment with required dependencies

# Define colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Set up virtual environment
echo -e "${YELLOW}Setting up virtual environment...${NC}"
python3 -m venv .venv

# Activate virtual environment
echo -e "${YELLOW}Activating virtual environment...${NC}"
source .venv/bin/activate

# Upgrade pip
echo -e "${YELLOW}Upgrading pip...${NC}"
pip install --upgrade pip

# Install dependencies
echo -e "${YELLOW}Installing dependencies from requirements.txt...${NC}"
pip install -r requirements.txt

echo -e "${GREEN}Setup complete!${NC}"
echo -e "${YELLOW}To activate the virtual environment, run:${NC}"
echo -e "source .venv/bin/activate"
echo -e "${YELLOW}To run the Buttondown sync script:${NC}"
echo -e "python .github/scripts/buttondown_sync.py"