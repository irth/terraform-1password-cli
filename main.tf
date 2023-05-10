data "external" "this" {
  program = ["${path.module}/get_secrets.py"]
  query   = { q = jsonencode(var.secrets) }
}

output "secrets" {
  description = "Secrets extracted from 1Password. Reflects the structure of the \"secrets\" input variable."
  sensitive   = true
  value       = jsondecode(data.external.this.result["o"])
}
