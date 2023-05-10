variable "secrets" {
  description = "Mapping of secret names to op:// paths. Can contain nested mappings."
  type        = map(any)
  default     = {}
}
