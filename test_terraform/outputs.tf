output "webservers_ip_addresses_output" {
  value = aws_instance.devops106_terraform_abishake_webserver_tf[*].public_ip
}

output "database_ip_addresses_output" {
  value = aws_instance.devops106_terraform_abishake_db_tf[*].public_ip
}
