from rest_framework import serializers

class SignupSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    phone_num = serializers.CharField()
    date_start = serializers.DateField()
    date_end = serializers.DateField()
    hotel_num = serializers.IntegerField()