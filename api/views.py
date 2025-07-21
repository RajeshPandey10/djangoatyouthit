
from employee.models import Employee
from .serializer import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404

class Employees (APIView):
    def get(self,request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post (self,request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Employee  created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"message": "Failed to create employee", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class EmployeeDetail (APIView):
    def get_object(self,pk):
        try:
            return Employee.objects.get(pk=pk)
        
        except Employee.DoesNotExist:
            raise Http404
    def get(self, request, pk,):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def delete(self,request,pk):
        employee = self.get_object(pk)
        employee.delete()
        return Response({"message": "employee deleted successfully"}, status=status.HTTP_204_NO_CONTENT)




    
       