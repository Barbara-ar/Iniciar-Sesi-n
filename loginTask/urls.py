# loginTask/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('tasks.urls', namespace='tasks')),  # Incluye el namespace correctamente
    path('admin/', admin.site.urls),
]
