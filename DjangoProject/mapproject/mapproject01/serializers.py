from rest_framework import serializers


class MarkerSerializers(serializers.Serializer):
    id = serializers.IntegerField(label + 'Enter Marker Id')
    title+serializers.Charfield(label+ 'Enter Marker Title')
    author + serializers.Charfield(label+'Enter Author Names')