from django.urls import path
from . import views

urlpatterns = [
    path('', views.kis_pro_index, name="kis_pro_index"),
    path("<int:pk>/", views.kis_pro_detail, name="kis_pro_detail"),
    path('new/', views.kis_pro_newuser, name="kis_pro_newuser"),
    path("deletedoc/<int:pk>", views.kis_pro_deleteuser, name="kis_pro_deleteuser"),
    path("deletepat/<int:pk>", views.kis_pro_deletepatient, name="kis_pro_deletepatient"),
    path("deletereg/<int:pk>", views.kis_pro_deleteregistration, name="kis_pro_deleteregistration"),
    path("reg", views.kis_pro_registration, name="kis_pro_registration"),
    path("pathology/<int:pk>", views.kis_pro_pathology, name="kis_pro_pathology"),
    path("pathology/meet/<int:pk>/<int:caseid>", views.kis_pro_pathology_meet, name="kis_pro_pathology_meet"),
    path("pathology/newtnm/<int:pk>", views.kis_pro_new_tnm, name="kis_pro_new_tnm"),
    path("surgery/<int:pk>", views.kis_pro_surgery, name="kis_pro_surgery"),
    path("surgery/meet/<int:pk>/<int:caseid>", views.kis_pro_surgery_meet, name="kis_pro_surgery_meet"),
    path("surgery/newsurg/<int:pk>", views.kis_pro_new_surgery, name="kis_pro_new_surgery"),
    path("radiology/<int:pk>", views.kis_pro_radiology, name="kis_pro_radiology"),
    path("radiology/meet/<int:pk>/<int:caseid>", views.kis_pro_radiology_meet, name="kis_pro_radiology_meet"),
    path("radiology/newrad/<int:pk>", views.kis_pro_new_radio, name="kis_pro_new_radio"),
    path('newpatient', views.kis_pro_newpatient, name="kis_pro_newpatient"),
    path('<int:pk>/newcase', views.kis_pro_newcase, name="kis_pro_newcase"),
]
