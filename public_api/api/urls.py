from django.urls import path
from .views import PublicCandidateView

urlpatterns = [
    path('public/candidate/', PublicCandidateView.as_view(), name='public_candidate'),
]
