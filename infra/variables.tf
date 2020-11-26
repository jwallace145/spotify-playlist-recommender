variable region {
  default = "us-east-1"
}

variable vpc_cidr_block {
  default = "1.0.0.0/24"
}

variable public_subnet_cidr_block {
  default = "1.0.0.0/28"
}

variable public_subnet_az {
  default = "us-east-1a"
}

variable private_subnet_cidr_block {
  default = "1.0.0.16/28"
}

variable private_subnet_az {
  default = "us-east-1b"
}
