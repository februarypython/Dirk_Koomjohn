# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string

def index(request):
    return render(request, 'sf_app/index.html')

def create(request):
    if request.method == "POST":
        print "=========== POST data ================"
        request.session['name'] = request.POST['name']
        request.session['favlang'] = request.POST['favlang']
        request.session['location'] = request.POST['location']
        request.session['comment'] = request.POST['comment']
        return redirect("/process")

def welcome(request):
    print "=========== welcome ================"
    request.session['counter'] += 1
    return render(request, 'sf_app/welcome.html')
