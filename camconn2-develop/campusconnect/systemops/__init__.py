import psycopg2
import os
import time
import json
from pprint import pprint

from django.conf import settings
from django.core.cache import cache
import sqlite3


def get_db_conn1():
    conn = psycopg2.connect(
        dbname =    os.environ.get("RESUMEWEB_DBNAME"),
        user =      os.environ.get("RESUMEWEB_DBUSERNAME"),
        password =  os.environ.get("RESUMEWEB_DBPASS"),
        host =      os.environ.get("RESUMEWEB_DBHOST"),
        port =      os.environ.get("RESUMEWEB_DBPORT"),

    )

    return conn


