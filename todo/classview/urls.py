from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from classview import views

urlpatterns = [
    path('classview/', views.TodoList.as_view()),
    path('classview/<int:pk>/', views.TodoDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)