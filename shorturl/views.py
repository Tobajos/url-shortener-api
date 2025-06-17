from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ShortURL
from .serializers import ShortenSerializer
from django.shortcuts import get_object_or_404

class ShortenURLView(APIView):
    def post(self, request):
        serializer = ShortenSerializer(data=request.data)
        if serializer.is_valid():
            short_url = ShortURL.objects.create(original_url=serializer.validated_data['original_url'])
            return Response({"short_url": f"http://localhost:8000/api/expand/{short_url.short_code}/"}, status=201)
        return Response(serializer.errors, status=400)

class ExpandURLView(APIView):
    def get(self, request, short_code):
        short_url = get_object_or_404(ShortURL, short_code=short_code)
        return Response({"original_url": short_url.original_url})
