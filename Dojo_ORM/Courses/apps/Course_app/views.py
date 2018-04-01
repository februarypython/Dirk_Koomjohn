from django.shortcuts import render, redirect

from .models import Course, Description
from django.contrib import messages

#--- ROOT
def index(request):
    context = {
        "Courses_list": Course.objects.all()
        }

    return render(request, 'Course_app/index.html', context)

#--- 
def add_course(request):
    print "in create route: request.POST = ", request.POST

# validate in models.py
    errors = Course.objects.basic_validator(request.POST)
    if len(errors):
        print "************* validation errors ***********"
#       for tag, error in errors.iteritems():
#            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        cn = request.POST['course_name']
        dt = request.POST['desc_text']
        dc = Description.objects.create(desc_text = dt)
        cc = Course.objects.create(name = cn, desc_text = dc)
        
        return redirect('/')

#--- /courses/<id>/destroy  *** Make sure user wants to delete
def destroy(request, id):
    context = {
        "the_course":Course.objects.get(id=id)
        }
    print "*****context******", context
    return render(request, 'Course_app/delete.html', context)

#--- /course/<id>/erase    *** delete a course after user review
def erase(request, id):
    dc = Course.objects.get(id=id)
    dc.delete()
    return redirect('/')