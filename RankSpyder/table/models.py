from django.db import models

# Create your models here.

class ACTableCache(models.Model):
    group = models.ForeignKey('users.Group',on_delete=models.CASCADE)
    student = models.ForeignKey('users.Student', on_delete=models.DO_NOTHING)

    signin = models.IntegerField(default=0)
    ak = models.IntegerField(default=0)
    
    detial = models.CharField(max_length=100)

class RankTableCache(models.Model):
    group = models.ForeignKey('users.Group',on_delete=models.CASCADE)
    student = models.ForeignKey('users.Student', on_delete=models.DO_NOTHING)

    detial = models.CharField(max_length=100)