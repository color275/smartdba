#!/bin/bash

echo "export AWS_CONTAINER_CREDENTIALS_RELATIVE_URI=$AWS_CONTAINER_CREDENTIALS_RELATIVE_URI" >> /root/.profile

# echo "MYSQL_HOST = $MYSQL_HOST" >> ./config.ini

# echo "export DB_MYSQL_HOST=$DB_MYSQL_HOST" >> /root/.profile
# echo "export DB_MYSQL_PORT=$DB_MYSQL_PORT" >> /root/.profile

# Migrate Database
python3 manage.py migrate --noinput


# Collect Staticfiles
# python3 manage.py collectstatic --noinput

# Run Gunicorn (WSGI Server)

# gunicorn --bind 0.0.0.0:8000 mysite.wsgi:application
python3 manage.py runserver 0.0.0.0:8000

tail -f /dev/null

/bin/bash