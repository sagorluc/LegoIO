from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseServerError
from django.core.mail import send_mail


def show_email_data(request):
    if request.method == 'POST':
        try: 
            csv_file = request.FILES['csv_file']
            if not csv_file.name.endswith('.csv'):
                messages.error(request, 'Only CSV files are supported.')
                return render(request, 'mail_form.html')
            
            clean_emails = []
            for line in csv_file:
                email = line.decode('utf-8').strip()
                if email:
                    clean_emails.append(email)
            
            print(clean_emails, 'line 31')  
            
            context = {
                'clean_emails': clean_emails,

            }
            messages.success(request, 'All the email displayed successfully.')
            template ='show_email_data.html'
            return render(request, template, context)
        
        except Exception as e:
            return HttpResponseBadRequest(f"(Upload_file) An error occurred : {str(e)}")
    
    else:
        template ='show_email_data.html'
        return render(request, template)
    
    