from django.urls import path, include
from .views import MealViewset, RatingViewset
from rest_framework import routers

app_name = 'meals'

router = routers.DefaultRouter()
router.register(r'meals', MealViewset, basename='meals')
router.register(r'rating', RatingViewset, basename='rating')

urlpatterns = [
    path('api/', include(router.urls)),
]




