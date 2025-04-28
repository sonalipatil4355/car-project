from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
import json

file = open(r'C:\Users\sonal\Desktop\Django\car project\app\car.json','r')
json_data=file.read()
py_data=json.loads(json_data)

car=py_data["car"]
def home(request):
    context={
        'car':car
    }
    return render(request,'home.html',context )

def about(request,n):
    context={
        'car':car[n-1],   
    }
    return render(request,'about.html',context)


def contact(request):
    return render(request,'contact.html')

def service(request):
    return render(request,'service.html')

