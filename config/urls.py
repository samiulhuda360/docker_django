from django.contrib import admin
from django.urls import path
from studentApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', StudentListView.as_view(), name='student'),
]
