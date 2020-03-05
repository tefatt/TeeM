from rest_framework import serializers

from api.models import AnswerModel


class AnswerSerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    def create(self, validated_data):
        pass

    class Meta:
        model = AnswerModel
        fields = ('id', 'name', 'is_correct')
        extra_kwargs = {'id': {'read_only': False}}
