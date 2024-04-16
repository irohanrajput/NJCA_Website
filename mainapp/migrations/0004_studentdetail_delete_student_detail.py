# Generated by Django 5.0.4 on 2024-04-14 14:26

import mainapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_alter_student_detail_date_of_birth'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('standard', models.CharField(max_length=50, verbose_name='Standard')),
                ('section', models.CharField(max_length=10, verbose_name='Section')),
                ('father_name', models.CharField(max_length=100, verbose_name="Father's Name")),
                ('date_of_birth', models.DateField(verbose_name='Date of Birth')),
                ('address', models.TextField(verbose_name='Address')),
                ('contact_number', models.CharField(max_length=15, verbose_name='Contact Number')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('admission_date', models.DateField(auto_now_add=True, verbose_name='Admission Date')),
                ('grade', models.CharField(max_length=10, verbose_name='Grade')),
                ('student_id', models.CharField(default=mainapp.models.generate_student_id, max_length=10, unique=True, verbose_name='Student ID')),
            ],
        ),
        migrations.DeleteModel(
            name='student_detail',
        ),
    ]