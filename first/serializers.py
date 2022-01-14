from rest_framework import serializers

from first.models import post


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = post
        fields = '__all__'
