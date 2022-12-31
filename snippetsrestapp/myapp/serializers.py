from rest_framework import serializers
from .models import snippets

class user_serializer(serializers.ModelSerializer):
    class Meta:
        model=snippets
        fields='__all__'
