from .views import AuthUserAPIView, LoginAPIView, RegisterAPIView
from django.urls import path

urlpatterns = [
    path('register', RegisterAPIView.as_view(), name="register"),
    path('login', LoginAPIView.as_view(), name="login"),
    path('user', AuthUserAPIView.as_view(), name="user"),
]
