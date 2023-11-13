from .models import meal, rating
from rest_framework import serializers
class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model= meal
        fields= ('id', 'title', 'description')
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model= rating
        fields= ('id', 'user', 'stars', 'meal')