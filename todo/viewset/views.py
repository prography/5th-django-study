from classview.models import Todo
from classview.serializers import TodoSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
    def perform_create(self, serializer):
        serializer.save()