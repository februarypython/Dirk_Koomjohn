from __future__ import unicode_literals
from django.db import models

# import "re" module for REGEX
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['fname']) < 2:
            errors["first_name"] = "First name should be at least 2 characters"
        if len(postData['lname']) < 2:
            errors["last_name"] = "Last name should be at least 2 characters"
        if len(postData['email']) < 1:
            errors["email"] = "No email address entered"
        elif not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Email address is invalid"
        elif User.objects.filter(email=postData['email']).exists():
			errors["email"] = "Email address already exists"
        return errors

    def update_validator(self, postData):
        find_id = postData["id"]
        u =  User.objects.get(pk=find_id)
        errors = {}
        if u.first_name <> postData["fname"]:
            if len(postData['fname']) < 3:
                errors["first_name"] = "First name should be more than 2 characters"
            else:
                print "update_validation: fname changed and passes validation -- saving ", postData["fname"]
                u.first_name = postData["fname"]
                u.save()
        if u.last_name <> postData["last_name"]:
            if len(postData['lname']) < 3:
                errors["lname"] = "Last name should be more than 2 characters"
            else:
                print "update_validation: lname changed and passes validation -- saving ", postData["lname"]
                u.last_name = postData["lname"]
                u.save()
        if u.email <> postData["email"]:
            if len(postData['email']) < 1:
                errors["email"] = "An email address must be entered"
            elif not EMAIL_REGEX.match(postData['email']):
                errors["email"] = "Invalid email address format"
            elif User.objects.filter(email=postData['email']).exists():
                errors["email"] = "Email address already exists"
            else:
                print "Updated Email:", postData["email"]
                u.email = postData["email"]
                u.save()
        return errors

    def create_user(self, first_name, last_name, email):
        user = self.create(first_name=first_name, last_name=last_name, email=email)
        return user
        
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 #connect an instance of UserManager to our User model overwriting the old hidden objects key with a new one with extra properties
    objects = UserManager()