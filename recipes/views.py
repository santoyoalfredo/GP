from django.contrib.auth import get_user_model
from .models import Recipe
from recipes.serializers import *
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

class IsUserOrReadOnly(permissions.BasePermission):

    # Check for owner permissions
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user == request.user

class UserViewSet(viewsets.ModelViewSet):

    # Get all users
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    # Display a user's recipes (e.g. /users/{pk}/recipes/)
    @action(detail=True, serializer_class=RecipeSerializer)
    def recipes(self, request, pk=None):

        recipes = Recipe.objects.filter(user=self.kwargs['pk'])
        serializer = self.get_serializer(recipes, many=True)
        return Response(serializer.data)

class RecipeViewSet(viewsets.ModelViewSet):

    # Get all recipes
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly]

    # Assign user to created recipe based on logged in user
    def perform_create(self, serializer):
        serializer.save(user=request.user)
