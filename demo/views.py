from django.shortcuts import render
from .models import Image

# Create your views here.
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