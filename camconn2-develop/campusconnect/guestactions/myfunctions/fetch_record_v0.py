import psycopg2
import os
import time
import json
from pprint import pprint

from django.conf import settings
from django.core.cache import cache
from .check_db_conn import get_db_conn1


# 100% functional
##************************************
# def fetch_order_records_v0(tracking_id, email_add):
#     conn = get_db_conn1()
#     print('nothing wrong here line104')

#     query3 = """select 
#                 rm.title, 
#                 rm.sku, 
#                 rm.processing_status, 
#                 rm.tracking_id,
#                 pm.guest_login_email_address
#         from resumeweb_mcart rm
#         inner join resumeweb_mcompleted_purchase pm
#         on rm.mcompleted_purchase_id = pm.id 
#         where 
#             rm.purchased = true 
#             and rm.tracking_id = %s
#             and pm.guest_login_email_address = %s;
#         """


#     query4 = """select 
#                 rm.title, 
#                 rm.sku, 
#                 rm.processing_status, 
#                 rm.tracking_id,
#                 pm.guest_login_email_address
#         from resumeweb_mcart rm
#         inner join resumeweb_mcompleted_purchase pm
#         on rm.mcompleted_purchase_id = pm.id 
#         where 
#             rm.purchased = true 
#             and rm.tracking_id = %s;
#         """
#         #     --and pm.guest_login_email_address = %s;
#         # """



#     cursor = conn.cursor()
#     start = time.time()
#     cursor.execute(query4, (tracking_id,))
#     # cursor.execute(query1)
#     raw_data = cursor.fetchall()
#     # raw_data = [('contact@dataflightit.com',), ('contact@dataflightit.com',), ('legouser0177@gmail.com',), ('contact@dataflightit.com',), ('contact@dataflightit.com',), ('contact@dataflightit.com',), ('contact@dataflightit.com',), ('contact@dataflightit.com',), ('contact@dataflightit.com',), ('contact@dataflightit.com',), ('contact@dataflightit.com',), ('contact@dataflightit.com',), ('contact@dataflightit.com',), ('contact@dataflightit.com',), ('mangopeople00@proton.me',), ('xyz67192@gmail.com',), ('contact@dataflightit.com',), ('contact@dataflightit.com',)]
#     end = time.time()
#     print("\nquery exec time:", end-start)
#     # print(raw_data)

#     return raw_data
