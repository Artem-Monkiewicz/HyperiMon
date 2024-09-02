from myapp.views import project_list, project_create
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', project_list, name='project_list'),
    path('create/', project_create, name='project_create'),
]

#sms new