from django.urls import path
from rest_framework_simplejwt import views

from .views import MyTokenObtainPairView

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view()),
    path('token/refresh/', views.TokenRefreshView.as_view()),
    path('token/verify/', views.TokenVerifyView.as_view()),
]
