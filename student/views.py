from urllib import request
from venv import create
from django.shortcuts import render
from django.http import JsonResponse
from .models import Student
from rest_framework.decorators import api_view
from api.serializer import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
@api_view(['GET','POST'])
def studentView(request):
    if request.method == 'GET':
        # Fetch all students        
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Student created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"message": "Failed to create student", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH', 'DELETE'])
def studentDetailView(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({"message": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PATCH':
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Student updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"message": "Failed to update student", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response({"message": "Student deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

def studentViewTemplates(request):
    students = Student.objects.all()
    return render(request, 'Student.html', {'students': students})
# def studentDetailViewTemplates(request, pk):
#         student = Student.objects.get(pk=pk)
    
        

def student_create(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        name = request.POST.get('name')
        faculty = request.POST.get('faculty')

        # Check if student_id already exists
        if Student.objects.filter(student_id=student_id).exists():
            students = Student.objects.all()
            return render(request, 'Student.html', {
                'students': students,
                'error': f'Student with ID "{student_id}" already exists. Please use a different ID.'
            })

        try:
            student = Student(student_id=student_id, name=name, faculty=faculty)
            student.save()
            students = Student.objects.all()
            return render(request, 'Student.html', {
                'students': students,
                'message': 'Student created successfully'
            })
        except Exception as e:
            students = Student.objects.all()
            return render(request, 'Student.html', {
                'students': students,
                'error': f'Error creating student: {str(e)}'
            })
    
    return render(request, 'create_student.html')  # Render a form for creating a student




