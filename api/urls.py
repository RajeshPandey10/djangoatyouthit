from django.urls import path, include
from . import views
urlpatterns = [
    path('students/', include('student.urls')),  # Include student app URLs
    path('employee/',views.Employees.as_view()),
    path('employee/<int:pk>/',views.EmployeeDetail.as_view()),
]
