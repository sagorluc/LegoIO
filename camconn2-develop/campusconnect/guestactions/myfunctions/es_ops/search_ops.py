from ..es_config.check_connection import get_es_connection
import logging
logger = logging.getLogger(__name__)

# Querying data
def fetch_data(user_query):
	es_conn = True #get_es_connection()
	if es_conn:
		query = {
		    "query": { 
		    	"match": {
		    		"title": { "query": user_query }
		    	}
		    }
		}

		results = es_connection.es_client.search(index="mango", body=query)
		logger.warning(results)
		return results
	else:
		results = "es_conn is NOT TRUE"
	

# 100% Functional
# GET mango/_search/
# {
#    "query":{
#       "match": {
#         "title": { "query": "how to format my profilev" }
#       }
#    }
# }
