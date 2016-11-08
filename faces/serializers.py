from rest_framework import serializers

class FacesSerializer(serializers.Serializer):
    def __init__(self, *args, **kwargs):
        super(FacesSerializer, self).__init__(*args, **kwargs)
        self.fields['url'] = serializers.CharField(required=False)
        self.fields['window'] = serializers.CharField(required=False)
