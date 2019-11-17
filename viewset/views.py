from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets

from fbv.models import Todo
from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    # @action(detail=True, renderer_classes=[renderers.StatisHTMLRenderer])
    # def highlight(self, request, *args, **kwargs):
    #     item = self.get_object()
    #     return Response(item.highlighted)

    # def perform_create(self, serializer):
    #     serializer.save()
    # 외래키를 넣을게 아니라면 굳이 작성할 필요가 없었던거지 ?