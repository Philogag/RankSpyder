from django.urls import path

from . import views

app_name = 'contest'
urlpatterns = [
    path('', views.view_all, name='view_all'),
    path('new/', views.add_contest, name="new"),
    path('<int:contest_id>/', views.view_index, name='view_index'),
    path('<int:contest_id>/submitions/', views.view_submitions, name='view_submitions'),
    path('<int:contest_id>/rank/', views.view_rank, name='view_rank'),

    path('<int:contest_id>/flush_submition/', views.flush_submition, name="flush_submition"),
    path('<int:contest_id>/flush_rank/', views.flush_rank, name="flush_rank"),
]