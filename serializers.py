from rest_framework import serializers
from .models import Company



class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'client_name', 'created_at','created_by']