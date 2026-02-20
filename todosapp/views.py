from rest_framework import generics
from django.contrib.auth.models import User
from .serializer import RegisterSerializer

#from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Todo
from .serializer import TodoSerializer

from rest_framework.viewsets import ModelViewSet


from django_filters.rest_framework import DjangoFilterBackend
class TodoViewSet(ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status']

class TodoViewSet(viewsets.ModelViewSet):
#def get_queryset(self):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_context(self):
        return {"request": self.request}
    

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    