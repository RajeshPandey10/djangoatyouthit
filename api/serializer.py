# serializer
from rest_framework import serializers
from student.models import Student
from employee.models import Employee
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    pass