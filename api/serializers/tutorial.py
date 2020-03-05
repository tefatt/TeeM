from rest_framework import serializers
from api.models import TutorialModel


class TutorialSerializer(serializers.ModelSerializer):

    class Meta:
        model = TutorialModel
        fields = ['id', 'name', 'content']
