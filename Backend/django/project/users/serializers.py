from rest_framework import serializers

class SignupSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    password1 = serializers.CharField()
    password2 = serializers.CharField()

class SigninSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField()