import os

## Localhost
# ELASTIC_SEARCH_URL      = "http://localhost:9200/"

## Bonsai
ELK_BASE_URL       = 'https://{username}:{password}@{host_ip}:{host_port}'
ELASTIC_SEARCH_URL = ELK_BASE_URL.format(
    username = os.environ.get('ES_ACCESS_KEY'),
    password = os.environ.get('ES_ACCESS_SECRET'),
    host_ip  = os.environ.get('ES_HOST'),
    host_port= os.environ.get('ES_PORT')
)

## Elasticsearch
# cloud_id="mango:dXMtY2VudHJhbDEuZ2NwLmNsb3VkLmVzLmlvJDNjYTdjZmZkMDlkODQ3N2RhNzQ3YTM0MzViZDY0YjllJGRkY2VkMTM0NTA1MjQxZDRhMmI5NDAwOGI0Yjk0NGFm"
# ELASTIC_SEARCH_URL = ELK_BASE_URL.format(
#     username='zupcr6llya',
#     password='c180rdjz1y',
#     host_ip='https://mango.es.us-central1.gcp.cloud.es.io',
#     host_port='443'
# )

## connection string
ELASTICSEARCH_DSL = {
    'default': {
        'hosts': [ELASTIC_SEARCH_URL]
    },
}
