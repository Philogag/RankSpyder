from django.db import models

# Create your models here.

from contest.models import PLATFORM_OPTIONS

class Group(models.Model):
    name = models.CharField(default="", max_length=50)
    platformNum = models.IntegerField(default=0)
    platforms = models.CharField(max_length=100)

    needFlash = models.BooleanField(default=False)
    lastAccess = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
    contestNum = models.IntegerField(default=0)
    
    contestIds = models.CharField(default="", max_length=100)
    problemNumList = models.CharField(default="", max_length=100)
    userNumList = models.CharField(default="", max_length=100)

    hint = models.CharField(default="", max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.name


class Student(models.Model):
    schoolId = models.IntegerField(default=0)
    name = models.CharField(default="", max_length=50)

    hint = models.CharField(default="", max_length=100, null=True, blank=True)
    
    def __str__(self):
        return str(self.schoolId) + "-" + self.name

######################
# 一对多
class StudentIdLink(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)

    platform = models.CharField(choices=PLATFORM_OPTIONS, max_length=50)
    username = models.CharField(default="", max_length=20)
