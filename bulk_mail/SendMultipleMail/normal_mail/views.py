from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseServerError
from django.core.mail import send_mail
from django.conf import settings
from normal_mail.mail_content import send_bulk_mail_async, send_bulk_mail_normal
from normal_mail.mail_content import EmailThread
import os
TEMP_DIR_GENERAL    = 'siteshared/layout/'

def view_homepage(request):
    template = 'homepage.html'
    return render(request, template)
    
def upload_csv_and_send_mail(request):
    if request.method == 'POST':
        try: 
            if not 'csv_file'  in request.FILES:
                messages.error(request, 'No csv file ')
                return redirect('upload_and_send_mail')
            
            csv_file = request.FILES['csv_file']
            subject = request.POST.get('subject')
            msg_body = request.POST.get('message')
            
            print(subject, 'line 23')
            print(msg_body, 'line 24')
            
            if not csv_file.name.endswith('.csv'):
                messages.error(request, 'Only CSV files are supported.')
                return render(request, 'mail_form.html')
            
            clean_emails = []
            for line in csv_file:
                email = line.decode('utf-8').strip()
                if email:
                    clean_emails.append(email)
            
            print(clean_emails, 'line 31')  
            
            if clean_emails and subject and msg_body:       
                # send_bulk_mail_normal(request, subject, msg_body, clean_emails)
                send_bulk_mail_async(request, subject, msg_body, clean_emails)
                status = 'done'
            else:
                status = 'failed'
            
            context = {
                'clean_emails': clean_emails,
                'status': status,
            }
            template ='mail_form.html'
            return render(request, template, context)
            # return redirect('upload_and_send_mail')
        
        except Exception as e:
            return HttpResponseBadRequest(f"(upload_csv_and_send_mail) An error occurred : {str(e)}")
    
    else:
        context = {
        'clean_emails': [],  # Empty list by default for initial page load
        'status': '',
        }
        template ='mail_form.html'
        return render(request, template, context)
