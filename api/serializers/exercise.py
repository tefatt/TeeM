from rest_framework import serializers
from api.models import ExerciseModel, TestSheetModel, LanguageModel, QuestionModel
from api.serializers import QuestionSerializer, LanguageSerializer
from api.serializers.test_sheet import TestSheetSerializer

'''source=question_data'''


class ExerciseSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)
    test_sheet = TestSheetSerializer(many=False)
    '''
        def create(self, validated_data):
            exercise = ExerciseModel.objects.create(validated_data)
            for q in validated_data.get('question_data'):
                question = QuestionModel.objects.create(q, exercise=exercise)
                for a in q.get('answer'):
                    AnswerModel.objects.create(a, question=question)
    '''

    def create(self, validated_data):
        data = validated_data['name']
        exercise = ExerciseModel.objects.create(name=data)
        for q in validated_data.get('question_data'):
            question = QuestionModel.objects.create(q, exercise)

    class Meta:
        model = ExerciseModel
        fields = ('name', 'questions', 'material_url', 'test_sheet')
