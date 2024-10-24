---
title: "Tagging Cloud Run services via terraform"
date: 2024-10-24T12:41:55+13:00

categories:
  - Technology
  - TIL
---

Today I learned the magic incantation to apply a GCP Resource Manager tag to a Cloud Run service via terraform:

```terraform
resource "google_tags_location_tag_binding" "service" {
  parent    = "//run.googleapis.com/projects/PROJECT_NUMER/locations/REGION/services/SERVICE_NAME"
  tag_value = "tagValue/TAG_ID"
  location  = "REGION"
}
```

This came about while I was trying to [create a public Cloud Run service within an organisation with domain restricted sharing policies enabled](https://cloud.google.com/blog/topics/developers-practitioners/how-create-public-cloud-run-services-when-domain-restricted-sharing-enforced).
Rather than YOLO-ing it via the CLI/console as that post suggests, I wanted to create the tags, values and bindings via terraform.

Translating the tag, value and policy into terraform was straightforward. Applying the tag to the project containing my function was not too much
more effort (via the `tag_binding_values` input of the [project-factory module](https://registry.terraform.io/modules/terraform-google-modules/project-factory/google)) either, but as in the post, I wanted to scope the tag more specifically to the Cloud Run service.

Binding the tag to the project happens via the `google_tags_tag_binding` terraform resource. So swapping out the project resource name for the
service should be a quick and easy change, right? Not for me.

In the end, I ended up using the Chrome web inspector to spy on what the Cloud Console was doing when tagging the service via the UI, and then
resorted to a bunch of manual API requests to arrive at the two crucial peices of the puzzle:
1. The parent field must start with the `run.googleapis.com` service name, not the `cloudresourcemanager.googleapis.com` string
   that is used when applying a tag to a project or folder. This is shown in the original post if you read the CLI example given carefully...
   If you use the wrong parent value, you'll get an error along the lines of:
   `Must be a valid One Platform resource name of a tag compatible regional resource`.
2. The API request has to be made to a regional endpoint like `us-west1-cloudresourcemanager.googleapis.com` not the default global endpoint at `cloudresourcemanager.googleapis.com`. If you get this wrong, you'll see errors along the lines of: `Must be a valid One Platform resource name of a tag-compatible global resource. Did you forget to specify the correct location?`. Getting terraform to use the regional endpoint, requires using the
 `google_tags_location_tag_binding` resource instead of `google_tags_tag_binding`.

With those discoveries made, several hours later, everything works as expected. As simple and obvious as it seems in hindsight, it wasn't at the
time and the relevant docs are all pretty sparse and distributed. Hopefully this post will save someone else some time... if that's
you, please [drop me a note](mailto:hi@mattb.nz) and let me know :)

For completeness, the overall set of terraform resources to re-create the setup from the original post looks something like:
```terraform
// Restrict external sharing - iam.allowedPolicyMemberDomains except for tagged resources
module "allowedPolicyMemberDomains" {
  source  = "terraform-google-modules/org-policy/google//modules/org_policy_v2"
  version = "~> 5.2.0"

  policy_root     = "organization"
  policy_root_id  = var.org_id
  constraint      = "iam.allowedPolicyMemberDomains"
  policy_type     = "list"

  rules = [
    {
      enforcement = true # deny-all default
      allow       = ["principalSet://iam.googleapis.com/organizations/ORGANIZATION_NUMBER"]
    },
    {
      enforcement = false # allow-all default
      conditions = [
        {
          title       = "allowAllUsersIngress"
          description = "Allow public ingress from tagged resources"
          expression  = "resource.matchTagId('${google_tags_tag_key.allUsersIngress.id}', '${google_tags_tag_value.allUsersIngressTrue.id}')"
          location    = "allowAllUsersIngress"
        }
      ]
    },
  ]
}

resource "google_tags_tag_key" "allUsersIngress" {
  parent      = "organizations/${var.org_id}"
  short_name  = "allUsersIngress"
  description = "Grants resource ability to allow allUsers to access it."
}
resource "google_tags_tag_value" "allUsersIngressTrue" {
  parent      = "tagKeys/${google_tags_tag_key.allUsersIngress.name}"
  short_name  = "True"
  description = "Grants resource ability to allow allUsers to access it."
}

resource "google_tags_location_tag_binding" "service" {
  parent    = "//run.googleapis.com/projects/PROJECT_NUMER/locations/REGION/services/SERVICE_NAME"
  tag_value = google_tags_tag_value.allUsersIngressTrue.id
  location  = "REGION"
}
```