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
    actor = ActorSerializer()
    repo = RepoSerializer()

    class Meta:
        model = Event
        fields = '__all__'

    def create(self, validated_data):
        actor_data = validated_data.pop('actor')
        repo_data = validated_data.pop('repo')
        event = Event.objects.create(**validated_data)
        actor, actor_created = Actor.objects.get_or_create(id=actor_data.get('id'))
        if actor_created:
            actor.save(**actor_data)
        repo, repo_created = Repo.objects.get_or_create(id=repo_data.get('id'))
        if repo_created:
            actor.save(**repo_data)
        event.actor = actor
        event.repo = repo
        event.save()
        return event
