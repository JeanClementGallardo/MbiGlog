from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="ngs_home"),
    path('pipeline/',views.pipeline,name="ngs pipeline home"),
    path('pipeline/fastqc-<int:id_request>/', views.fastqc, name="ngs fastqc"),
    path('phylo/', views.phylo_align, name="phylogenic pipeline hub")
]
