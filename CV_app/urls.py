from django.contrib import admin
from django.urls import path, include

# different name, yeah
urlpatterns = [
    path('', include(('CV.urls', 'CV'), namespace='CV'))
]
