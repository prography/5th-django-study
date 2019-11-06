from django.urls import path, include

urlpatterns = [
    path('', include('classview.urls')),
    path('', include('funcview.urls')),
    path('', include('mixin.urls')),
    path('', include('viewset.urls')),
]
