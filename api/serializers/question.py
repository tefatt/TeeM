from rest_framework import serializers

from api.models import QuestionModel
from api.serializers import AnswerSerializer


class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True)
    name = serializers.CharField()
    time_point = serializers.FloatField()

    def create(self, validated_data):
        pass

    class Meta:
        model = QuestionModel
        fields = ('name', 'answer', 'time_point','max_score')
