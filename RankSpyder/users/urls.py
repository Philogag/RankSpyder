from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('', views.group_list, name='group_list'),
    path('newgroup/', views.newgroup, name="newgroup"),
    path('<int:group_id>/', views.group_detial, name='group_detial'),
    # path('<int:contest_id>/submitions/', views.view_submitions, name='view_submitions'),
    
    path('<int:contest_id>/delgroup/', views.delgroup, name='delgroup'),
]