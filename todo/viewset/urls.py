from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from viewset.views import TodoViewSet

todo_list = TodoViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

todo_detail = TodoViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

urlpatterns = [
    path('viewset/', todo_list),
    path('viewset/<int:pk>/', todo_detail),
]
