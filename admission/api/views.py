from admission.models import Admission
from rest_framework import viewsets
from admission.api.serializer import Admissionser

class UserViewSet(viewsets.ModelViewSet):
    queryset = Admission.objects.all()
    serializer_class = Admissionser