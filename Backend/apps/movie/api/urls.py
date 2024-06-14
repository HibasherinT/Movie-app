from django.urls import path
from ..views import moviee

urlpatterns = [
    path('moviee/', moviee.as_view(), name='moviee'),
    path('moviee/<int:pk>/', moviee.as_view(), name='moviee')
]