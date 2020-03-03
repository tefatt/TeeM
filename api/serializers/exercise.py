from rest_framework import serializers
from api.models import ExerciseModel, TestSheetModel, LanguageModel, QuestionModel, AnswerModel
from api.serializers import QuestionSerializer, LanguageSerializer
from api.serializers.test_sheet import TestSheetSerializer

'''source=question_data'''


class ExerciseSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)
    test_sheet = TestSheetSerializer(many=False)

    def create(self, validated_data):
        ordered_dict = validated_data['test_sheet']
        name = ordered_dict['name']
        '''
        pk of testsheet is missing, test_sheet_id-->HARDCODED
        '''
        exercise = ExerciseModel.objects.create(name=validated_data['name'], test_sheet_id=1)
        for q in validated_data['questions']:
            question = QuestionModel.objects.create(name=q['name'], max_score=q['max_score'], exercise_id=exercise.id)
            for a in q['answer']:
                answ = AnswerModel.objects.create(name=a['name'], question_id=question.id)
        return exercise

    def update(self, instance, validated_data):
        '''i = 0
        j = 0
        '''
        exercise = ExerciseModel.objects.get(id=instance.id)
        exercise.name = validated_data['name']
        exercise.save()
        '''
        for q in validated_data['questions']:
            #question = QuestionModel.objects.get(id=instance.questions[i].id)
            validated_data['questions']['name'] = 'name'
            #question.max_score = q['max_score']
            #question.save()
            i += 1
            for a in q['answer']:
                answ = AnswerModel.objects.get(id=instance.answers[j].id)
                answ.name = a['name']
                answ.save()
                j += 1'''
        return exercise


    class Meta:
        model = ExerciseModel
        fields = ('id','name', 'questions', 'material_url', 'test_sheet')
