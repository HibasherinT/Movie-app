from django.urls import path
from ..views import RegisterView, LoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name="sign_up"),
    path('login/', LoginView.as_view(), name='log_in')
]