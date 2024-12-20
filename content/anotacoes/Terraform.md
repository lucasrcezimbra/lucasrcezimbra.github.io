---
title: "Terraform"
date: 2023-08-15
lastmod: 2024-10-31
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
Moved to My Toolbox - [Terraform](https://toolbox.cezimbra.me/lists/terraform/),
