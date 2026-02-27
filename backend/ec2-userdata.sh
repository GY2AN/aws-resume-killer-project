#!/bin/bash

# Update packages
yum update -y

# Install Python 3
yum install python3 -y

# Install pip
yum install python3-pip -y

# Install Git
yum install git -y

# Clone your repository
cd /home/ec2-user
git clone https://github.com/YOUR_USERNAME/aws-resume-killer-project.git

cd aws-resume-killer-project/backend

# Install dependencies
pip3 install flask pymysql

# Set environment variables
export DB_HOST="rk-database.chk8omi8012t.ap-south-1.rds.amazonaws.com"
export DB_USER="admin"
export DB_PASSWORD="rztaDbg2STCA2i7pqjVi"
export DB_NAME="appdb"

# Run app
python3 app.py
