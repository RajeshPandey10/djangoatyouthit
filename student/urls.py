from django.urls import path
from . import views

urlpatterns = [
    path('', views.studentView),
    path('<int:pk>/', views.studentDetailView,), 
    path('templates/', views.studentViewTemplates, name='student-list'),  
    path('create/', views.student_create, name='student-create'), 
]

