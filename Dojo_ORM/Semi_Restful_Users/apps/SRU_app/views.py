from django.shortcuts import render, HttpResponse, redirect

from .models import User
from django.contrib import messages

#--- ROOT
def index(request):
    context = {
        "user_list": User.objects.all()
        }
    return render(request, 'SRU_app/index.html', context)

#--- /users/new
def new(request):
    return render(request, 'SRU_app/new.html')

#--- /users/create --- create user/info
def create(request):
    print "in create route: request.POST = ", request.POST

# validations from models
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/users/new')
    else:
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email']
        user = User.objects.create_user(first_name, last_name, email)
        return redirect('/users/'+str(user.id))

#--- /users/<id>   --- display user info
def show(request, id):
    context = {
        "user": User.objects.get(id=id)
        }
    return render(request, 'SRU_app/show.html', context)

#--- /users/<id>/edit  --- display and allow for user edit
def edit(request, id):
    context = {
        "user": User.objects.get(id=id)
        }
    return render(request, 'SRU_app/edit.html', context)

#--- /users/update   --- process edited info
def update(request, id):
    # Use validation and update performed in models.py

    errors = User.objects.update_validator(request.POST)
    print "in update route, returned from validator with errors=", errors
    # if errors in updated values found, return to /users/<id>/edit and display errors
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/users/'+id+'/edit')
    else:
        return redirect('/users/'+id)

#--- /users/<id>/destroy   --- delete a user
def destroy(request, id):
    user_id = int(id)
    print "in destory with user_id=", user_id
    u = User.objects.get(id=user_id)
    u.delete()
    return redirect('/users')