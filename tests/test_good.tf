resource "aws_instance" "the_machine" {
  ami           = "ami-12345"
  instance_type = "t2.micro"

  availability_zone = "us-east-1a"
  subnet_id = "subnet-11zxcvxcv"
  vpc_security_group_ids = [
    "${aws_security_group.the_group.id}",
    "${aws_security_group.the_other_group.id}"
  ]
  tags = {
    Terraform   = true
  }
}
