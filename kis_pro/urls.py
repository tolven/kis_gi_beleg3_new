from django.urls import path
from . import views

urlpatterns = [
    path('', views.kis_pro_index, name="kis_pro_index"),
    path("<int:pk>/", views.kis_pro_detail, name="kis_pro_detail"),
    path('new/', views.kis_pro_newuser, name="kis_pro_newuser"),
    path("<int:pk>/delete", views.kis_pro_deleteuser, name="kis_pro_deleteuser"),
    path("reg", views.kis_pro_registration, name="kis_pro_registration"),
    path("pathology", views.kis_pro_pathology, name="kis_pro_pathology"),
    path("surgery", views.kis_pro_surgery, name="kis_pro_surgery"),
    path("radiology", views.kis_pro_radiology, name="kis_pro_radiology"),
    path('newpatient/', views.kis_pro_newpatient, name="kis_pro_newpatient"),
]