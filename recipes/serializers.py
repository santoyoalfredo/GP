from django.contrib.auth import get_user_model
from .models import Recipe
from rest_framework import serializers

class RecipeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Recipe
        fields = '__all__'
        read_only_fields = ['user']

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name']

    id = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)
