from rest_framework import serializers


class GeoJsonSerializer(serializers.Serializer):
    type = serializers.CharField(required=False)
    features = serializers.ListField(required=False)