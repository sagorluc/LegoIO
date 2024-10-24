from django.urls import path
from normal_mail.views import (
    # upload_csv_and_send_mail, 
    view_homepage,
    upload_and_send_mail,
)
from normal_mail.show_mail_data import show_email_data

urlpatterns = [
    path('', view_homepage, name='homepage'),
    # path('upload_and_send_mail/', upload_csv_and_send_mail, name='upload_and_send_mail'),
    path('upload_csv/', upload_and_send_mail, name='upload_csv'),
    path('all_email/', show_email_data, name='show_email_data'),
   
]
