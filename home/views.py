from django.shortcuts import render
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.

# httpresponse is used to print the string in general we use template on that place
def index(request):
    # context={'variable':'hehehe'}
    return render(request,'index.html')
def projects(request):
    return render(request,'projects.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    if request.method=='POST':
     name_surname=request.POST.get('name_surname')
     email=request.POST.get('email')
     phone=request.POST.get('phone')
     message=request.POST.get('message')
     contact=Contact(name_surname=name_surname,email=email,phone=phone,message=message,date=datetime.today())
     contact.save()
     mail=f'''
     {email}
     {phone}
     {message}
     '''
     send_mail(name_surname,mail,'',['vystudent68@gmail.com'])
     messages.success(request,'Your Message has been submitted!!')
    return render(request,'contact.html')

    
