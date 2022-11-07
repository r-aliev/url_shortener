from rest_framework import serializers

from .models import URLMapper


class URLMapperSerializer(serializers.ModelSerializer):
    class Meta:
        model = URLMapper
        fields = '__all__'
