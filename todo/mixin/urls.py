from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from mixin import views

urlpatterns = [
    path('mixin/', views.TodoList.as_view()),
    path('mixin/<int:pk>/', views.TodoDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)