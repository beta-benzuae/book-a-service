import json
import datetime

from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.conf import settings
 
from web.functions import generate_form_errors
from web.forms import ServiceForm

def index(request):
    
    form = ServiceForm()
    
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            data= form.save(commit=False)
            data.save()
            
            mailto = 'digital@benzuae.com'
            
            subject = 'Message From Book a Service'
            message = f'''
            Name:  {data.name}, 
            Contact: {data.phone}
            Email: {data.email}
            Selected Date:  {data.date}
            Time Taken :  {data.time}
            Vehicle Number:  {data.vehicle_number},
            Kilometers Driven :  {data.kms_driven}
            Service Needed: {data.message}
            
            
            -- 
            This e-mail was sent from a contact form on Almaraghi Website.'''

            
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [mailto, ]
            send_mail( subject, message, email_from, recipient_list )
            
            
                

            response_data = {
                "status" : "success",
                "title" : "Successfully Submitted",
                "message" : "Booking Successfully Created.",
                "redirect": "true",
                "stable" : "false",
                "redirect_url": reverse('web:redirect')
            }
        else: 
            message = generate_form_errors(form, formset=False)
            
            response_data = {
                
            "status" : "error",
            "title" : " Oops! Try Again ",
            "message" : str(message) ,
        }  

        return HttpResponse(json.dumps(response_data),content_type='application/javascript')
    else:

        context = {
            "title": " Book A service",
            "form":form,
            
        }
    return render(request, "index.html", context)


def redirect(request):
    
       return HttpResponseRedirect("http://benzuae.com")
