---
title: "Terraform"
date: 2023-08-15T07:30:00-03:00
lastmod: 2024-06-05
---
## CI/CD
- [Atlantis](https://www.runatlantis.io/)
- [Terraform Cloud](https://cloud.hashicorp.com/products/terraform)


## Packer
- `amazon-chroot` vs `amazon-ebs`
    - `amazon-ebs` is slower, needs to run an instance and create an image.
    - `amazon-chroot` is faster because it uses Kernel isolation to create the image, but parallel builds don't work well.

## Testing
- [Terratest](https://terratest.gruntwork.io/) - Go library that provides patterns and helper functions for testing infrastructure, with 1st-class support for Terraform, Packer, [Docker]({{< ref "Docker" >}}), Kubernetes, AWS, GCP, and more.

## Tools
- [Terraformer](https://github.com/GoogleCloudPlatform/terraformer) - (reverse Terraform) generates tf/json and tfstate files based on existing infrastructure.
- [Infracost](https://github.com/infracost/infracost) - Cloud cost estimates in pull requests