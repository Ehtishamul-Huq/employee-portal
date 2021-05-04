from .serializers import EmployeeSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Employee

class EmployeeView(APIView):
    serializer_class = EmployeeSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'data':serializer.data}, status=status.HTTP_200_OK)

    def get(self,request):
        queryset = Employee.objects.all()
        serializer = self.serializer_class(queryset,many=True)
        return Response({'data':serializer.data}, status=status.HTTP_200_OK)

class EmployeeUpdate(APIView):
    serializer_class = EmployeeSerializer
    def get(self,request,pk):
        queryset = Employee.objects.get(id=pk)
        serializer = self.serializer_class(queryset)
        return Response({'data':serializer.data}, status=status.HTTP_200_OK)

    def put(self,request,pk):
        queryset = Employee.objects.get(id=pk)
        serializer = self.serializer_class(instance=queryset,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({'data':serializer.data}, status=status.HTTP_200_OK)

    def delete(self,request,pk):
        queryset = Employee.objects.get(id=pk)
        queryset.delete()
        return Response({'message': 'Employee is deleted'}, status=status.HTTP_200_OK)