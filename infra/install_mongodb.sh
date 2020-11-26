#! /bin/bash
sudo su
aws s3 cp s3://jwalls-fun-bucket/mongo/mongodb-org-4.4.repo /etc/yum.repos.d/mongodb-org-4.4.repo
sudo yum install -y mongodb-org
sudo systemctl start mongod
echo "hello, world!" >> test.txt