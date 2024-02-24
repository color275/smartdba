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
    'BMS': {
        'ENGINE': 'django.db.backends.mysql',
        # 'ENGINE': 'mysql.connector.django',
        'NAME': BMS_NAME,
        'USER': BMS_USER,
        'PASSWORD': BMS_PASSWORD,
        'HOST': BMS_HOST,
        'PORT' : BMS_PORT,
        'OPTIONS': {
            "unix_socket": "/applications/mysql/tmp/mysql.sock",
        }
    },
    #'homenet': {
    #  'ENGINE': 'sql_server.pyodbc',
    #  'NAME': HOMENET_NAME,
    #  'USER': HOMENET_USER,
    #  'PASSWORD': HOMENET_PASSWORD,
    #  'HOST': HOMENET_HOST,
    #  'PORT' : HOMENET_PORT,
    #  "OPTIONS": {
    #      "driver": "ODBC Driver 11 for SQL Server",
    #      "unicode_results": True,
    #      "host_is_server": True,
    #  },
    #},
    'metadb': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': META_NAME,
        'USER': META_USER,
        'PASSWORD': META_PASSWORD,
    },
    'DHUB11': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': DHUB_NAME,
        'USER': DHUB_USER,
        'PASSWORD': DHUB_PASSWORD,
    },
    'DHUB12': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': DHUB_NAME,
        'USER': DHUB_USER,
        'PASSWORD': DHUB_PASSWORD,
    },
    'SMTCPRD11': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': SMTC_NAME,
        'USER': SMTC_USER,
        'PASSWORD': SMTC_PASSWORD,
    },
    'DEVSMTC': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': DSMTC_NAME,
        'USER': DSMTC_USER,
        'PASSWORD': DSMTC_PASSWORD,
    },
    'DEVEC': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': DWEB_NAME,
        'USER': DWEB_USER,
        'PASSWORD': DWEB_PASSWORD,
    },
    'iam': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': IAM_NAME,
        'USER': IAM_USER,
        'PASSWORD': IAM_PASSWORD,
    },
    'sms': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': SMS_NAME,
        'USER': SMS_USER,
        'PASSWORD': SMS_PASSWORD,
    },
}