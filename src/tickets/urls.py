from django.urls import path

from . import views

urlpatterns = [
    path('tickets/', views.ListCreateTicketAPIView.as_view()),
    path('tickets/<int:pk>/', views.UpdateTicketAPIView.as_view()),
]
