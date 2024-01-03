from datetime import datetime
from .db_ops import get_db_conn1
import logging
logger = logging.getLogger(__name__)

def check_buyer_exists_v0(email_add):
    conn = get_db_conn1()
    logger.warning('nothing wrong here line104')

    query4 = """select rm.email
    			from resumeweb_buyerlistguest rm
    			where rm.email = %s;"""

    cursor = conn.cursor()
    # start = time.time()
    cursor.execute(query4, (email_add,))
    # cursor.execute(query1)
    raw_data = cursor.fetchall()
    # end = time.time()
    # print("\nquery exec time:", end-start)
    # print(raw_data)

    return raw_data	


def check_buyer_exists(conn,email_add):
    # conn = get_db_conn1()
    # print('nothing wrong here line104')

    query4 = """select rm.email
    			from resumeweb_buyerlistguest rm
    			where rm.email = %s;"""

    cursor = conn.cursor()
    # start = time.time()
    cursor.execute(query4, (email_add,))
    # cursor.execute(query1)
    raw_data = cursor.fetchall()
    # end = time.time()
    # print("\nquery exec time:", end-start)
    # print(raw_data)

    return raw_data	

def check_order_status(email_add, tracking_id):
	conn = get_db_conn1()
	if conn is not None:
		# check if any buyer exists with this email_add
		buyer_true = check_buyer_exists(conn,email_add)
		# check if any order exists with this tracking_id
		if buyer_true:
			return True
	else:
		return HttpResponse("db connection lost")



# if buyer_true and order_true:

#   # check if db connection is active
#   conn = get_db_conn1()
#   # if true, send user info to fetch record
#   if conn:
#     end_date = datetime.now().strftime('%Y-%m-%d')
#     order_status = fetch_record(conn,tracking_id, email_add, end_date)
#     if len(order_status) == 0:
#       return HttpResponse("no records found from user info")
#     else:
#       context = {
#           'posted_info': [tracking_id, email_add],
#           'order_status': order_status,
#           'form_order_search': self.form_class()
#       }
#       return render(
#         request=self.request,
#         template_name=self.template_name,
#         context=context
#       )
#   else:
