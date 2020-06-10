from django.shortcuts import render

# Create your views here.

from .models import Group

def group_list(request):
    return render(request, 'user/group_list.html', {'groups': Group.objects.all()})

def group_detial(request, group_id):
    pass

def newgroup(request):
    pass

def delgroup(request, group_id):
    pass