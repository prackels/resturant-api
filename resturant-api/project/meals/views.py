from django.shortcuts import render
from .seializers import MealSerializer, RatingSerializer
from .models import meal, rating
from rest_framework import viewsets
class MealViewset(viewsets.ModelViewSet):
    queryset= meal.objects.all()
    serializer_class= MealSerializer
class RatingViewset(viewsets.ModelViewSet):
    queryset= rating.objects.all()
    serializer_class= RatingSerializer