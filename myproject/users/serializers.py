from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['last_name', 'name', 'father_name', 'date_of_birth', 
                  'number', 'number_polis', 'email', 'password', 'role']

    def create(self, validated_data):
        user = User(**validated_data)
        user.save()
        return user

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email уже существует.")
        return value

    def validate_password(self, value):
        if len(value) < 6:
            raise serializers.ValidationError("Пароль должен содержать не менее 6 символов.")
        return value
    

    