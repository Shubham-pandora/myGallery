from django.shortcuts import render
from .models import Image
from django.core.mail import send_mail

# Create your views here.
send_mail(
    'Subject ',
    'Hello',
    'shubham@email.beta-wspbx.com', # Sender email address
    ['shubham@email.beta-wspbx.com'], # List of recipient email addresses
    fail_silently=False, # Set to True to ignore errors when sending email
)

def index(request):
    data = Image.objects.all()
    print("----------------")
    for i in data:
        print(i,type(i))
        print(i.title,type(i.title))
        print(i.photo,type(i.photo))
        print(i.photo.url)
    print("----------------")
    print("----------------")
    context = {
        'data' : data
    }
    return render(request,"display.html", context)