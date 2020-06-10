from django.db import models

# Create your models here.

PLATFORM_OPTIONS = [
    ("VJ", "vjudge"),
    ("NC", "newcoder"),
]

STATUS_OPTIONS = [
    (1, "Accept"),
    (0, "Ignore"),
    (-1, "Wrong")
]

class Contest(models.Model):
    platform = models.CharField(default="", choices=PLATFORM_OPTIONS, max_length=5)

    contestId = models.IntegerField(default=0)  # contest id on platform
    contestName = models.CharField(default = "",max_length=50)
    password = models.CharField(default = "", max_length=50, blank=True, null=True)
    
    problemNum = models.IntegerField(default=0)
    startTime = models.DateTimeField(auto_now=False, auto_now_add=False)
    endTime = models.DateTimeField(auto_now=False, auto_now_add=False)

    hint = models.CharField(default="", max_length=100, blank=True, null=True)
    

class Submition(models.Model):
    localContestId = models.IntegerField(default=0)
    userId = models.CharField(max_length=20)

    problemId = models.IntegerField(default=0)
    submitTime = models.IntegerField(default=0)
    status = models.IntegerField(choices=STATUS_OPTIONS)

class Rank(models.Model):
    localContestId = models.IntegerField(default=0)
    userId = models.CharField(max_length=20)

    ac = models.IntegerField(default=0)
    time = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)

    ac_detail = models.CharField(default = "", max_length=100)
