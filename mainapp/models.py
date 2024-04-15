from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

def generate_student_id():
    last_student = StudentDetail.objects.order_by('-id').first()
    if last_student:
        last_id = int(last_student.student_id)
        new_id = last_id + 1
    else:
        new_id = 202400000
    return str(new_id).zfill(9)


class StudentDetail(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    standard = models.CharField(max_length=50, verbose_name='Class')
    father_name = models.CharField(max_length=100, verbose_name="Father's Name")
    date_of_birth = models.DateField(verbose_name='Date of Birth')
    address = models.TextField(verbose_name='Address')
    contact_number = models.CharField(max_length=15, verbose_name='Contact Number')
    email = models.EmailField(unique=True, verbose_name='Email')
    admission_date = models.DateField(auto_now_add=True, verbose_name='Admission Date')
    student_id = models.CharField(max_length=10, unique=True, default=generate_student_id, verbose_name='Student ID')
        
    def __str__(self):
        return self.name