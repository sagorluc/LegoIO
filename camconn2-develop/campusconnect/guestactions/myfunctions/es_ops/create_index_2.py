# import json
# import logging
# import os
# from typing import Dict

# import numpy as np
# import pandas as pd
# from elasticsearch import Elasticsearch

# logging.basicConfig(filename="es.log", level=logging.INFO)

# ES_HOSTS 	= [""]
# ES_PORT 	= ""
# ES_USERNAME = os.environ["ES_ACCESS_KEY"]
# ES_PASSWORD = os.environ["ES_ACCESS_SECRET"]

# def create_index(self, index_name: str, mapping: Dict) -> None:
#     """
#     Create an ES index.
#     :param index_name: Name of the index.
#     :param mapping: Mapping of the index
#     """
#     index_name = ""
#     mapping = ""
#     logging.info(f"Creating index {index_name} with the following schema: {json.dumps(mapping, indent=2)}")
#     self.es_client.indices.create(index=index_name, ignore=400, body=mapping)

# PUT /mango2082


# # 100% Functional
# # PUT mango2082/_doc/1
# # { "title": "i need to format my resume", "description": "very effective resume analysis service that gives you the control you need" }
