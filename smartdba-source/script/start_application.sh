#!/usr/bin/env bash

cd /home/ec2-user/build/
source /home/ec2-user/build/project-venv/bin/activate
# nohup python /home/ec2-user/build/manage.py runserver 0.0.0.0:8000 &
python /home/ec2-user/build/manage.py runserver 0.0.0.0:8000 > /dev/null 2> /dev/null < /dev/null &
