from rest_framework.decorators import api_view
from rest_framework.response import Response
from userapp.models import Student
from userapp.serializers import StudentSerializer


@api_view(["POST"])
def create_student(request):
    serializer=StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message":"Student added successfully",
            "data":serializer.data
        })
    return Response(serializer.errors)

@api_view(["GET"])
def fetchStudents(request):
    students=Student.objects.all()
    serializer=StudentSerializer(students,many=True)
    return Response(serializer.data)

@api_view(["GET"])
def fetchStudent(request,id):
    try:
        student=Student.objects.get(id=id)
    except Student.DoesNotExist:
        return Response({"message":"student not Found"})

    serializer=StudentSerializer(student)
    return Response(serializer.data)

@api_view(["PUT"])
def updateStudent(request,id):
    try:
        student=Student.objects.get(id=id)
        print(id)
    except Student.DoesNotExist:
        return Response({
            "error":"Student not Found"
        })
    
    serializer=StudentSerializer(student,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message":"Student Updated",
            "data":serializer.validated_data

        })
    else:
        return Response(serializer.errors)

@api_view(["PATCH"])
def partialUpdateStudent(request,id):
    try:
        student=Student.objects.get(id=id)
        print(id)
    except Student.DoesNotExist:
        return Response({
            "error":"Student not found"
        })

    serializer=StudentSerializer(student,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "meassage":"Student Updated",
            "data":"serializer.validated_data"
        })
    else:
        return Response(serializer.errors)

@api_view(["DELETE"])
def deleteStudent(request,id):
    try:
        student=Student.objects.get(id=id)
    except Student.DoesNotExist:
        return Response({"message": "Student Not Found"})
    student.delete()
    return Response({"message":"Student Deleted successful....."})

