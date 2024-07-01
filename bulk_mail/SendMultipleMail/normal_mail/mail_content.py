from django.contrib import messages
from django.shortcuts import render, redirect
from datetime import datetime
from django.http import HttpResponse, HttpResponseServerError, HttpResponseRedirect
from django.core.mail import send_mail, EmailMessage, BadHeaderError
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
import logging
import asyncio
import os
logger = logging.getLogger(__name__)
import concurrent.futures
import threading
from threading import Thread

TEMP_DIR_GENERAL = 'siteshared/layout/'


# ================================ SEND ASYNC MAIL ======================================
async def send_async_mail(request, subject, msg_body, clean_emails):
    start_time = datetime.now()

    try:
        loop = asyncio.get_event_loop()
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [loop.run_in_executor(executor, send_bulk_mail, request, subject, msg_body, clean_email) for clean_email in clean_emails]

            for future in concurrent.futures.as_completed(futures):
                try:
                    await future  # Wait for completion or catch exceptions
                except Exception as e:
                    logger.error(f"Email sending failed: {e}")

        end_time = datetime.now()
        duration = end_time - start_time
        logger.info(f"Emails sent in {duration.seconds} seconds")
        return HttpResponse("Bulk emails sent successfully")
    
    except Exception as e:
        logger.error(f"Error sending bulk emails: {e}")
        return HttpResponseServerError("Error sending bulk emails")


# ================================ SEND BULK MAIL ASYNC ==================================
class EmailThread(threading.Thread):
    def __init__(self, subject, html_content, recipient_list):
        self.subject = subject
        self.recipient_list = recipient_list
        self.html_content = html_content
        threading.Thread.__init__(self)

    def run(self):
        try:
            from_eamil = settings.EMAIL_HOST_USER
            msg = EmailMessage(self.subject, self.html_content, from_eamil, self.recipient_list)
            msg.content_subtype = "html"
            msg.send()
            logger.info(f"Email sent to {self.recipient_list}")
            
        except Exception as e:
            logger.error(f"Error sending email: {e}")
            
            

def send_bulk_mail_async(request, subject, msg_body, clean_emails):
    start_time = datetime.now()  
    result_dict = {}
    context = {
        'subject': subject,
        'msg': msg_body
    }
    
    template = 'send_bulk_mail.html'
    html_content = render_to_string(template, context)
    
    try:
        if clean_emails:
            for recipient_email in clean_emails:
                if recipient_email:
                    print(recipient_email, '=============== async email ================')
                    thread = EmailThread(subject, html_content, [recipient_email])
                    thread.start()
                    status = 'done'
                    # thread.join()  # Wait for the thread to finish before proceeding
                
            end_time = datetime.now()
            total_duration = end_time - start_time
            messages.success(request, f'Asynchronous email sent successfully. Total duration of async exucation is {total_duration.seconds} seconds')
            print(f'Asynchronous total duration is {total_duration.seconds} seconds')
        
        else:
            logger.warning("Recipient list is empty (send_bulk_mail_async).")
            messages.warning(request, 'Recipient list is empty (send_bulk_mail_async).')

    except Exception as e:
        logger.error(f"Error sending email: {e}")
        messages.error(request, f"An error occurred while sending email (send_bulk_mail_async): {e}")
        
        
    clean_emails_with_status = [(email, result_dict.get(email, 'Success')) for email in clean_emails]
    print(clean_emails_with_status, clean_emails, 'line 79')
    
    context = {
        'status': status,
        'clean_emails': clean_emails,
        'clean_emails_with_status': clean_emails_with_status
    }
    template = 'mail_form.html'
    return render(request, template, context)



# ================================ SEND BULK MAIL NORMAL =================================
def send_bulk_mail_normal(request, subject, msg_body, clean_emails):
    start_time = datetime.now()
    from_email = settings.EMAIL_HOST_USER
    print(from_email, '=========== line 48 ==================')
    context = {
        'subject': subject,
        'msg': msg_body
    }
    
    template = 'send_bulk_mail.html' 
    html_content = render_to_string(template, context)
    
    try:
        if clean_emails:
            for recipient_email in clean_emails:
                print(recipient_email, '=============== line 60 ================')
                send_mail(
                    subject=subject, 
                    message=msg_body, 
                    from_email=from_email, 
                    recipient_list=[recipient_email],  # Send email to a single recipient
                    html_message=html_content,
                    fail_silently=False,
                )
                logger.info(f"Email sent to {recipient_email}")
                
            end_time = datetime.now()
            total_duration = end_time - start_time
            messages.success(request, f'Email sent successfully. Total duration is {total_duration.seconds} seconds')
            print(f'Total duration is {total_duration.seconds} seconds')
        
        else:
            logger.warning("Recipient list is empty")
            messages.warning(request, 'Recipient list is empty. send_bulk_mail')

    except Exception as e:
        logger.error(f"Error sending email: {e}")
        messages.error(request, f"An error occurred while sending email send_bulk_mail : {e}")

    template = 'mail_form.html'
    return render(request, template)
    