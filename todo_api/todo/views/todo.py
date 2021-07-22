from rest_framework import viewsets

from ..models import Todo
from ..serializers import TodoSerializer


class TodoModelViewSet(viewsets.ModelViewSet):
    """actions: create, retrieve, update, partial_update, destroy, list"""
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
