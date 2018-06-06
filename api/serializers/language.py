from rest_framework import serializers

from api.models import LanguageModel


class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = LanguageModel
        fields = ('id', 'name')
