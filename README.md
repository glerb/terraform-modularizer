# Terraform Modularizer

![Tests](https://github.com/glerb/terraform-modularizer/workflows/Python%20application/badge.svg?branch=master)

Ever had to move Terraform code for existing resources into a module? What happens to those resources after you `terraform apply`? They get destroyed and recreated! Absurd. In order to prevent that nonsense, you need to use the `terraform state mv` command in the [Terraform CLI](https://www.terraform.io/docs/commands/state/index.html) to modify your state file to reflect the new module location of the resources. Except....you have to do it resource by resource! This package allows you to cut and paste the Terraform code for the resources into a single file and do a batch `terraform state mv`.

For usage, use the standard `-h` flag.
