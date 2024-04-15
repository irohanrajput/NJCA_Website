from django.urls import path
from .views import student_detailListCreate, student_detailRetrieveUpdateDestroy

urlpatterns = [
    path('students/', student_detailListCreate.as_view(), name='student_list_create'),
    
    path('students/<int:pk>/', student_detailRetrieveUpdateDestroy.as_view(), name='student_retrieve_update_destroy'),

]

