from rest_framework import serializers

class CustomerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    subject = serializers.CharField()
    message = serializers.DateField()
    