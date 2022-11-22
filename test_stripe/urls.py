
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('test_task.urls')),
    path('admin/', admin.site.urls),
]