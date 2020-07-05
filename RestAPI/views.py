# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from RestAPI.models import Event, Actor
from RestAPI.serializers import EventDetailSerializer, EventModelSerializer, ActorModelSerializer


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

    # @action(methods=['GET'], detail=False, url_path='actors/(?P<actor_id>[^/.]+)',)
    # def get_events_by_actor(self):


class RestApiDestroyViewSet(generics.DestroyAPIView):
    serializer_class = EventModelSerializer

    def delete(self, request, *args, **kwargs):
        Event.objects.all().delete()
        return Response({}, status=status.HTTP_200_OK)


class RestApiActorListViewSet(generics.ListAPIView):
    serializer_class = EventModelSerializer

    def list(self, request, *args, **kwargs):
        actor_id = kwargs.get('actor_id')
        queryset = Event.objects.filter(actor__id=actor_id)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RestApiActorUpdateViewSet(APIView):
    serializer_class = ActorModelSerializer
    queryset = Actor.objects.all()

    def put(self, request, *args, **kwargs):
        instance = get_object_or_404(Actor, pk=request.data.get('id'))
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(**serializer.validated_data)
        return Response(serializer.validated_data)
