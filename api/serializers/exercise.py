from rest_framework import serializers
from api.models import ExerciseModel, TestSheetModel, LanguageModel
from api.serializers import QuestionSerializer, LanguageSerializer


class ExerciseSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, source='question_data')
    test_sheet = serializers.SlugRelatedField(slug_field='name', read_only=True)


    def create(self, validated_data):
        pass

    #
    class Meta:
        model = ExerciseModel
        fields = ('name', 'questions', 'material_url', 'test_sheet')
