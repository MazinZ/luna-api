from rest_framework import serializers
from firebasetoken.models import *

class FirebaseTokenSerializer(serializers.ModelSerializer):
    firebasetoken = serializers.CharField(source='key')

    class Meta:
        model = FirebaseToken
        fields = (
            'firebasetoken',
        )