from rest_framework import serializers
from . models import UserInfo

class UserInfoSerializer(serializers.ModelSerializer):
    current_datetime = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S.%fZ")
    class Meta:
        model = UserInfo
        fields = '__all__'

    def get_github_link(self, obj):
        return "https://github.com/yourusername/django-user-api" 