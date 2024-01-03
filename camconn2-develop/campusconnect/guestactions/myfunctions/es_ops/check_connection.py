import json
import logging
import os

logger = logging.getLogger(__name__)

from elasticsearch import Elasticsearch
from elasticsearch.exceptions import ConnectionError

HOST_ADD = os.environ.get('ES_HOST')
PORT_ADD = os.environ.get('ES_PORT')
ACCESS_KEY = os.environ.get('ES_PORT')
SECRET_KEY = os.environ.get('ES_PORT')

def get_es_connection():
    try:
        es_client = Elasticsearch(
            [os.environ.get('ES_HOST')],
            http_auth=(os.environ.get('ES_ACCESS_KEY'), os.environ.get('ES_ACCESS_SECRET')),
            scheme="https",
            port=443,
        )
        logger.warning("elastic_client.ping() >>>{}".format(es_client))
        return es_client
    except ConnectionError as error:
        logger.warning("Elasticsearch Client Error:", error)
        es_client = Elasticsearch()
        return False

    