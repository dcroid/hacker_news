from rest_framework import serializers


class NewsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=512)
    url = serializers.URLField()
    created = serializers.DateTimeField()
