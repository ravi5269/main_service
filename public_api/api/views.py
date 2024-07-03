from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Candidate
from users.serializers import CandidateSerializer
from .middleware import APIKeyAuthentication

class PublicCandidateView(APIView):
    authentication_classes = [APIKeyAuthentication]

    def post(self, request):
        serializer = CandidateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        candidates = Candidate.objects.filter(user=request.user)
        serializer = CandidateSerializer(candidates, many=True)
        return Response(serializer.data)
