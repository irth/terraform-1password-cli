## terraform-1password-cli

[1Password](https://1password.com) offers an official [Terraform
provider](https://registry.terraform.io/providers/1Password/onepassword/latest),
however it requires setting up a [1Password Connect] server, for which I am too
lazy. (Especially given that I just want to use this to manage my personal
infra.)

This module only requires the [1Password
CLI](https://1password.com/downloads/command-line/) to be installed to work.

The `op://` URL syntax description can be found [here](https://developer.1password.com/docs/cli/reference/commands/read/).

### Example usage:

```terraform
module "op" {
  source = "./1password-cli"
  secrets = {
    ovh = {
      application_key    = "op://Terraform/ovh/application_key"
      application_secret = "op://Terraform/ovh/application_secret"
      consumer_key       = "op://Terraform/ovh/consumer_key"
    }
    vercel = {
      api_token = "op://Terraform/vercel/api_token"
    }
  }
}

provider "ovh" {
  application_key    = module.op.secrets.ovh.application_key
  application_secret = module.op.secrets.ovh.application_secret
  consumer_key       = module.op.secrets.ovh.consumer_key
  endpoint           = "ovh-eu"
}

provider "vercel" {
  api_token = module.op.secrets.vercel.api_token
}
```



<!-- BEGIN_TF_DOCS -->
## Requirements

No requirements.

## Providers

| Name | Version |
|------|---------|
| <a name="provider_external"></a> [external](#provider\_external) | n/a |

## Modules

No modules.

## Resources

| Name | Type |
|------|------|
| [external_external.this](https://registry.terraform.io/providers/hashicorp/external/latest/docs/data-sources/external) | data source |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_secrets"></a> [secrets](#input\_secrets) | Mapping of secret names to op:// paths. Can contain nested mappings. | `map(any)` | `{}` | no |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_secrets"></a> [secrets](#output\_secrets) | Secrets extracted from 1password. Reflects the structure of the "secrets" input variable. |
<!-- END_TF_DOCS -->
