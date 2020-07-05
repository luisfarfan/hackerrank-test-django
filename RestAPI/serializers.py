from rest_framework import serializers

from RestAPI.models import Actor, Event, Repo


class ActorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    login = serializers.CharField()
    avatar_url = serializers.CharField()


class RepoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    url = serializers.CharField()


class ActorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'


class RepoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repo
        fields = '__all__'


class EventModelSerializer(serializers.ModelSerializer):
    actor = ActorModelSerializer()
    repo = RepoModelSerializer()

    class Meta:
        model = Event
        fields = ('id', 'actor', 'repo', 'actor_event')


class EventDetailSerializer(serializers.ModelSerializer):
    # actor = ActorSerializer(required=True)
    # repo = RepoSerializer(required=True)

    class Meta:
        model = Event
        fields = '__all__'

    def create(self, validated_data):
        actor_data = validated_data.pop('actor')
        repo_data = validated_data.pop('repo')
        event = Event.objects.create(**validated_data)
        actor = Actor.objects.create(event=event, **actor_data)
        repo = Repo.objects.create(event=event, **repo_data)
        event.save()
        return event
