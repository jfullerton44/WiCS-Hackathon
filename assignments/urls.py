from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'assignments'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='pages/login.html'), name='login'),
    path('todo/', views.todoView.as_view(), name='todo'),
    path('createAssignment/', views.AssignmentCreateView.as_view(), name='create_assignment'),
    path('deleteAssignment/<slug:assignment_id>', views.delete_assignment, name='delete_assignment'),

]