from django.shortcuts import render,HttpResponse
from datetime import datetime
from app.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context={
        "variable":"Variable is set"
    }
    return render(request,"index.html",context)
def contact(request):
    if request.method== "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request,'Your message has been sent!')
    return render(request,"contact.html")
def about(request):
    return render(request,"about.html")
def sedan(request):
    return render(request,"sedan.html")
def hatchback(request):
    return render(request,"hatchback.html")
def suv(request):
    return render(request,"suv.html")
def supercar(request):
    return render(request,"supercar.html")