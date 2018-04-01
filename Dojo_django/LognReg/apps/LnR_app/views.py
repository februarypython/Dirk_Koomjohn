from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

#--- ROOT
def index(request):
    request.session.clear()
    return render(request, 'LnR_app/index.html')

#--- 
def register(request):
# validate in models.py
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        print "************* validation errors ***********", errors
        context = {
           "error_list": errors
           }
        return render(request, 'LnR_app/index.html', context)
    else:
        fn = request.POST['first_name']
        ln = request.POST['last_name']
        e = request.POST['email']
        pw = request.POST['password']
        bpw = bcrypt.hashpw(pw.encode(), bcrypt.gensalt())
        print "***password:", pw
        print "***bcrypt pw:", bpw

        User.objects.create(first_name = fn, last_name = ln, email = e, password = bpw)
 
        request.session['email'] = request.POST['email']
        return redirect('/success')

#--- 
def login(request):
    
    request.session['email'] = request.POST['email']
    User.objects.get(email=request.session['email'])

    bpw2 = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())

 #   if bpw2 != User.password:
 #       print "********************* passwords do not match ***************", bpw2, User.password
    #    messages.add_message(request, messages.INFO, "Invalid Password")
 #       return redirect('/')

    return redirect("/success")


#---/success
def success(request):
       
    context = {
        "logged_user": User.objects.get(email=request.session['email'])
    }
    return render(request, 'LnR_app/success.html', context)