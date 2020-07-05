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

    def update(self, instance, validated_data):
        instance.avatar_url = validated_data['avatar_url']
        instance.save()
        return instance


class RepoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repo
        fields = '__all__'


class EventModelSerializer(serializers.ModelSerializer):
    actor = ActorModelSerializer()
    repo = RepoModelSerializer()

    class Meta:
        model = Event
        fields = '__all__'


class EventDetailSerializer(serializers.ModelSerializer):
    actor = ActorSerializer(write_only=True)
    repo = RepoSerializer(write_only=True)

    class Meta:
        model = Event
        fields = '__all__'

    def create(self, validated_data):
        actor_data = validated_data.pop('actor')
        repo_data = validated_data.pop('repo')
        event = Event.objects.create(**validated_data)
        actor = Actor.objects.create(**actor_data)
        repo = Repo.objects.create(**repo_data)
        event.actor = actor
        event.repo = repo
        event.save()
        return event
