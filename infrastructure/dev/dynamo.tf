resource "aws_dynamodb_table" "message-board-dev" {
  name           = "message-board-dev"
  billing_mode   = "PROVISIONED"
  read_capacity  = 1
  write_capacity = 1
  hash_key       = "threadId"
  attribute {
    name = "threadId"
    type = "S"
  }
}