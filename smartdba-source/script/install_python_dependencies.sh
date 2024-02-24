#!/usr/bin/env bash
pip3 install virtualenv
sudo chown -R ec2-user:ec2-user /home/ec2-user/build
python3 -m virtualenv /home/ec2-user/build/project-venv
chown ec2-user:ec2-user /home/ec2-user/build/project-venv
chown ec2-user:ec2-user /home/ec2-user/build/project-venv/*
source /home/ec2-user/build/project-venv/bin/activate
pip install -r /home/ec2-user/build/requirements.txt