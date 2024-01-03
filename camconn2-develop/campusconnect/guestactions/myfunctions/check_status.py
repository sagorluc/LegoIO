from datetime import datetime
from systemops.db_conn import get_db_conn1
from .fetch_record import (
	fetch_record_buyerinfo,
	fetch_record_orderinfo
)


def check_order_status(email_add, tracking_id):
	conn = get_db_conn1()
	if conn is not None:
		# check if any buyer exists with this email_add
		buyer_true = fetch_record_buyerinfo(conn,email_add)
		if buyer_true:
			# check if any order exists with this tracking_id
			order_data = fetch_record_orderinfo(conn,tracking_id)
			return order_data
		else:
			return False
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
