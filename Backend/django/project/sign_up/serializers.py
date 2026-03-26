from rest_framework import serializers

class Sign_upSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    password_1 = serializers.CharField()
    password_2 = serializers.CharField()
