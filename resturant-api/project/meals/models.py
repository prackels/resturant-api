from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinLengthValidator
class meal(models.Model):
    title= models.CharField(max_length=50)
    description= models.TextField()

class rating(models.Model):
    meal= models.ForeignKey(meal, on_delete=models.CASCADE)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    stars= models.IntegerField(validators=[MinLengthValidator(1), MaxValueValidator(5)])
    