from __future__ import unicode_literals
from django.db import models

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors["first_name"] = "first name must be at least 3 characters in length"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "last name must be at least 3 characters in length"
        if len(postData['password']) < 8:
            errors["password"] = "password must be at least 8 characters in length"
        if postData['password'] != postData['pw_confirm']:
            errors["pw_confirm"] = "password does not match confirm"
	if len(postData['email']) < 6:
	    errors["email"] = "email incomplete"
        elif not EMAIL_REGEX.match(postData['email']):
            errors["email_format"] = "email invalid format"

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # *************************
    # Connect an instance of CourseManager to our Course model overwriting
    # the old hidden objects key with a new one with extra properties!!!
    # *************************
    objects = UserManager()

#    def __str__(self):
#        return "User Info:  %s %s" % (self.first_name, self.last_name)

