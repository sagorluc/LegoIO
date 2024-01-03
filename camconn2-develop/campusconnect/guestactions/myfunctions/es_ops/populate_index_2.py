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

# def populate_index(self, path: str, index_name: str) -> None:
#     """
#     Populate an index from a CSV file.
#     :param path: The path to the CSV file.
#     :param index_name: Name of the index to which documents should be written.
#     """
#     path = ""
#     index_name = ""
#     df = pd.read_csv(path).replace({np.nan: None})
#     logging.info(f"Writing {len(df.index)} documents to ES index {index_name}")
#     for doc in df.apply(lambda x: x.to_dict(), axis=1):
#         self.es_client.index(index=index_name, body=json.dumps(doc))
