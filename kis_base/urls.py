from django.urls import path
from . import views

urlpatterns = [
    path('', views.kis_base_landing, name='kis_base_landing'),
]
