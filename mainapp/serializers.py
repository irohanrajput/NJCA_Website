from rest_framework import serializers
from .models import StudentDetail

class student_detailSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDetail
        fields = '__all__'
        read_only_fields = ('student_id',)