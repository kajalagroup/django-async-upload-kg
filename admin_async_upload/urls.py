from django.urls import path

from . import views

urlpatterns = [
    path('upload/', views.admin_resumable, name='admin_resumable'),
]
