from django.db import models

from certificate.views import create_authentication_key

from course.models import Course
from student.models import Student



# Create your models here.

class Certificate(models.Model):
    # Colunas
    created_date = models.DateField(auto_now_add=True)
    authentication_key = models.CharField(
        max_length = 100,
        blank=True,
        editable=False,
        unique=True,
        default=create_authentication_key
    )
    
    # Colunas de Relacionamentos
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)