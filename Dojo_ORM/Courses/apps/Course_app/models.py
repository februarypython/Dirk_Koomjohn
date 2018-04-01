from __future__ import unicode_literals
from django.db import models

# import "re" module for REGEX
#import re
#EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['course_name']) < 6:
            errors["course_name"] = "Course must be at least 6 characters in length"
        if len(postData['desc_text']) < 15:
            errors["desc_text"] = "Course description must be at least 15 characters in length"
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # *************************
    # Connect an instance of CourseManager to our Course model overwriting
    # the old hidden objects key with a new one with extra properties!!!
    # *************************
    objects = CourseManager()

#    def __str__(self):
#        return "Course Info:  %s %s" % (self.name, self.desc_text)

class Description(models.Model):
    desc_text = models.CharField(max_length=255, default="")
    course = models.OneToOneField(Course, on_delete=models.CASCADE, primary_key=True,)
#    def __str__(self):
#        return self.desc_text
