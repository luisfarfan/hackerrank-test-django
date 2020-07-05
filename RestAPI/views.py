# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from RestAPI.models import Event
from RestAPI.serializers import EventDetailSerializer, EventModelSerializer


class RestApiViewSet(generics.ListCreateAPIView, generics.RetrieveAPIView):
    serializer_class = EventModelSerializer

    def get_queryset(self):
        queryset = Event.objects.all()
        return queryset

    def post(self, request, *args, **kwargs):
        serializer = EventDetailSerializer(data=request.data)
        if serializer.is_valid():
            event = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def get(self, request, *args, **kwargs):
    #     pass


class RestApiDestroyViewSet(generics.DestroyAPIView):
    serializer_class = EventModelSerializer

    def delete(self, request, *args, **kwargs):
        Event.objects.all().delete()
        return Response({}, status=status.HTTP_200_OK)


class RestApiActorViewSet(generics.ListAPIView):
    def list(self, request, *args, **kwargs):
        pass
