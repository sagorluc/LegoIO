from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseServerError
from django.core.mail import send_mail
from django.conf import settings
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from normal_mail.mail_content import send_bulk_mail_async, send_bulk_mail_normal
from normal_mail.mail_content import EmailThread
import os
TEMP_DIR_GENERAL    = 'siteshared/layout/'

def view_homepage(request):
    template = 'homepage.html'
    return render(request, template)

def upload_and_send_mail(request):
    context = {
        'clean_emails': [],
        'subject': '',
        'message': '',
    }

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'upload':
            csv_file = request.FILES.get('csv_file')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            
            if not subject and not message:
                subject = "Testing subject"
                message = "Testing message"

            if not csv_file or not csv_file.name.endswith('.csv'):
                messages.error(request, 'Upload a valid CSV file.')
            else:
                clean_emails = process_csv_file(csv_file)
                if not clean_emails:
                    messages.error(request, 'No valid emails found in CSV file.')
                else:
                    # store data in session
                    request.session['clean_emails'] = clean_emails
                    request.session['subject'] = subject
                    request.session['message'] = message

                    # update context with session data
                    context.update({
                        'clean_emails': clean_emails,
                        'subject': subject,
                        'message': message,
                    })

        elif action == 'send':
            clean_emails = request.session.get('clean_emails')
            subject = request.session.get('subject')
            message = request.session.get('message')
            
            if 'subject' in request.POST and 'message' in request.POST:
                subject = request.POST.get('subject')
                message = request.POST.get('message')
            
            print(clean_emails, 'line 59')
            print(subject, 'line 60')
            print(message, 'line 61')

            if clean_emails and subject and message:
                for email in clean_emails:
                    send_bulk_mail_async(request, subject, message, [email])
                messages.success(request, 'Emails sent successfully.')
            else:
                messages.error(request, 'Incomplete data. Upload a CSV file and provide subject/message.')

            return redirect('upload_csv')

    return render(request, 'mail_form.html', context)


def process_csv_file(csv_file): # Validation email
    clean_emails = []
    for line in csv_file:
        email = line.decode('utf-8').strip()
        if email:
            try:
                validate_email(email)
                clean_emails.append(email)
            except ValidationError:
                pass  # Skip invalid emails
    return clean_emails


# def upload_csv_and_send_mail(request):
#     if request.method == 'POST':
#         try: 
#             if not 'csv_file'  in request.FILES:
#                 messages.error(request, 'No csv file ')
#                 return redirect('upload_and_send_mail')
            
#             csv_file = request.FILES['csv_file']
#             subject = request.POST.get('subject')
#             msg_body = request.POST.get('message')
            
#             print(subject, 'line 23')
#             print(msg_body, 'line 24')
            
#             if not csv_file.name.endswith('.csv'):
#                 messages.error(request, 'Only CSV files are supported.')
#                 return render(request, 'mail_form.html')
            
#             clean_emails = []
#             for line in csv_file:
#                 email = line.decode('utf-8').strip()
#                 if email:
#                     clean_emails.append(email)
            
#             print(clean_emails, 'line 31')  
            
#             if clean_emails and subject and msg_body:       
#                 send_bulk_mail_normal(request, subject, msg_body, clean_emails)
#                 # send_bulk_mail_async(request, subject, msg_body, clean_emails)
#                 status = 'done'
#             else:
#                 status = 'failed'
            
#             context = {
#                 'clean_emails': clean_emails,
#                 'status': status,
#             }
#             template ='mail_form.html'
#             return render(request, template, context)
#             # return redirect('upload_and_send_mail')
        
#         except Exception as e:
#             return HttpResponseBadRequest(f"(upload_csv_and_send_mail) An error occurred : {str(e)}")
    
#     else:
#         context = {
#         'clean_emails': [],  # Empty list by default for initial page load
#         'status': '',
#         }
#         template ='mail_form.html'
#         return render(request, template, context)
