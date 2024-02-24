from .base import *

DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # 'ENGINE': 'mysql.connector.django',
        'NAME': MYSQL_NAME,
        'USER': MYSQL_USER,
        'PASSWORD': MYSQL_PASSWORD,
        'HOST': MYSQL_HOST,
        'PORT' : MYSQL_PORT,
        'OPTIONS': {
            "unix_socket": "/applications/mysql/tmp/mysql.sock",
        }
    },   
}