
from rest_framework import generics
from .models import StudentDetail
from .serializers import student_detailSerializer

class student_detailListCreate(generics.ListCreateAPIView):
    queryset = StudentDetail.objects.all()
    serializer_class = student_detailSerializer
    
class student_detailRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentDetail.objects.all()
    serializer_class = student_detailSerializer
    
