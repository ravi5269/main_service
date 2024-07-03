# users/urls.py
from django.urls import path
from .views import RegisterView, LoginView

from .views import CandidateView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),

    path('candidate/', CandidateView.as_view(), name='candidate'),

]
