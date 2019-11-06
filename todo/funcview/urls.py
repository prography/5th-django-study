from django.urls import path
from funcview import views

urlpatterns = [
    path('funcview/', views.todo_list),
    path('funcview/<int:pk>/', views.todo_detail),
]