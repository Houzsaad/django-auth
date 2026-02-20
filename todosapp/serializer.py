from django.contrib.auth.models import User

from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'completed', 'created_at']
        read_only_feilds = ['id', 'created_at']
    
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def create(self, validate_data):
        user = User.objects.create_user(
            username = validate_data['username'],
            password = validate_data['password']
        )
        user.save()
        return user

    def validate_title(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("Title must be at least 10 characters long.")
        return value

    def create(self, validated_data):
        request = self.context.get('request')
        #validated_data['user'] = request.user
        return super().create(validated_data)