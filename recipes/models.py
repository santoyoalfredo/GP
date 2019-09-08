from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    # Password is inherited from Django User model

class Step(models.Model):
    step_text = models.TextField()  # not_null is false by default
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, related_name='steps')

class Ingredient(models.Model):
    text = models.TextField()   # not_null is false by default
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, related_name='ingredients')

class Recipe(models.Model):
    name = models.CharField(max_length=60)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='recipes')
