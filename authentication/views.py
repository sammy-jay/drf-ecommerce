from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.response import Response

class HelloAuthView(generics.GenericAPIView):
    def get(self, request):
        return Response("Hello Auth", status=status.HTTP_200_OK)