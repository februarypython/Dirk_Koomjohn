# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited

print "+++++++++++ views +++++++++++++++"

def index(request):
  response = "Method for index!"
  return HttpResponse(response)

def new(request):
  response = "Method for new!"
  return HttpResponse(response)

def create(request):
  print "+++++++++++ create +++++++++++++++"
  return redirect("/")

def show(request, number):
  print "+++++++++++ show +++++++++++++++"
  return HttpResponse("Blog #" + number)

def edit(request, number):
  print "+++++++++++ edit +++++++++++++++"
  return HttpResponse("Edit Blog #" + number)

def destroy(request, number):
  print "+++++++++++ destroy +++++++++++++++"
  return redirect("/")