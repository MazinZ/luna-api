from rest_framework import serializers

class ExportSerializer(serializers.Serializer):
    def __init__(self, *args, **kwargs):
        super(ExportSerializer, self).__init__(*args, **kwargs)
        self.fields['content'] = serializers.DictField(required=True)
