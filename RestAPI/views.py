# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from RestAPI.serializers import EventDetailSerializer


class RestApiViewSet(generics.ListCreateAPIView, generics.RetrieveAPIView):
    serializer_class = EventDetailSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            event = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        pass

    def list(self, request, *args, **kwargs):
        pass


class RestApiDestroyViewSet(generics.DestroyAPIView):
    def delete(self, request, *args, **kwargs):
        pass


class RestApiActorViewSet(generics.ListAPIView):
    def list(self, request, *args, **kwargs):
        pass
