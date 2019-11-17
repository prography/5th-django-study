# from .views import TodoViewSet#, api_root

# from rest_framework import renderers
# from rest_framework.urlpatterns import format_suffix_patterns
# from django.urls import path

# todo_list = TodoViewSet.as_view({
#     'get':'list',
#     'post':'create'
# })
# todo_detail = TodoViewSet.as_view({
#     'get':'retrieve',
#     'put':'update',
#     'patch':'partial_update',
#     'delete':'destroy'
# })
# urlpatterns = format_suffix_patterns([
#     # path('', api_root),
#     path('todo/', todo_list, name='todo-list'),
#     path('todo/<int:pk>/', todo_detail, name="todo-detail"),
# ])

from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from snippets import views
from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'todos', views.TodoViewSet)
# router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]