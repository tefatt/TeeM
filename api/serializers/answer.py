from rest_framework import serializers

from api.models import AnswerModel


class AnswerSerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    def create(self, validated_data):
        pass

    class Meta:
        model = AnswerModel
        fields = ('name', 'is_correct')
