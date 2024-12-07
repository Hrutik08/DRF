from .models import Student
from .serializers import StudentSerializer
from rest_framework import  viewsets
from api.auth import CustomeAuthentication
from rest_framework.permissions import IsAuthenticated

class StudentModelViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    authentication_classes = [CustomeAuthentication]
    permission_classes = [IsAuthenticated]
