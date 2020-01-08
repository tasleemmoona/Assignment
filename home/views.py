from rest_framework import viewsets
from .serializers import StudentSerializer
from .models import student


class StudentViewSet(viewsets.ModelViewSet):
    queryset = student.objects.all().order_by('name')
    serializer_class = StudentSerializer