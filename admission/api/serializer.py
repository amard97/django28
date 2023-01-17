from admission.models import Admission
from rest_framework import serializers

class Admissionser(serializers.ModelSerializer):
    class Meta:
        model = Admission
        fields ='__all__'
