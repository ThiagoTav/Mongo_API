# serializers.py
from rest_framework import serializers
from .models import WeatherEntity

class WeatherSerializer(serializers.Serializer):
    temperature = serializers.FloatField()
    city = serializers.CharField(max_length=100, required=False)
    atmosphericPressure = serializers.CharField(max_length=100, required=False)
    humidity = serializers.CharField(max_length=100, required=False)
    weather = serializers.CharField(max_length=100, required=False)
    date = serializers.DateTimeField()

    def create(self, validated_data):
        return WeatherEntity(**validated_data)

    def update(self, instance, validated_data):
        instance.temperature = validated_data.get('temperature', instance.temperature)
        instance.city = validated_data.get('city', instance.city)
        instance.atmosphericPressure = validated_data.get('atmosphericPressure', instance.atmosphericPressure)
        instance.humidity = validated_data.get('humidity', instance.humidity)
        instance.weather = validated_data.get('weather', instance.weather)
        instance.date = validated_data.get('date', instance.date)
        return instance