resource "aws_s3_bucket" "message-board-web-dev" {
  bucket = "message-board-web-dev"

  tags = {
    Name        = "message-board-web-dev"
    Environment = "Dev"
  }
}

resource "aws_s3_bucket_website_configuration" "message-board-web-dev" {
  bucket = aws_s3_bucket.message-board-web-dev.id

  index_document {
    suffix = "index.html"
  }
}

resource "aws_s3_bucket_policy" "bucket_policy" {
  bucket = aws_s3_bucket.message-board-web-dev.id
  policy = data.aws_iam_policy_document.access.json
}

data "aws_iam_policy_document" "access" {
  statement {
    actions = [
      "s3:GetObject"
    ]
    principals {
      type = "AWS"
      identifiers = ["*"]
    }
    resources = ["${aws_s3_bucket.message-board-web-dev.arn}/*"]
  }
}

resource "aws_s3_bucket_public_access_block" "public_access" {
  bucket = aws_s3_bucket.message-board-web-dev.id

  block_public_acls       = true
  block_public_policy     = false
  ignore_public_acls      = true
}