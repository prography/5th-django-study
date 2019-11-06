from rest_framework import serializers
from classview.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'created', 'modified', 'complete', 'due_date']