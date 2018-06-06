from rest_framework import serializers
from api.models import UserModel, TestSheetModel, LanguageModel
from api.serializers import LanguageSerializer


class ExerciseSerializer(serializers.ModelSerializer):
    test_sheet = serializers.PrimaryKeyRelatedField(queryset=TestSheetModel.objects.all())
    languages = LanguageSerializer(many=True)

    # def create(self, validated_data):
    #     ad_target = AdTargetModel.objects.create(ad=validated_data.get('ad'),
    #                                              genders=validated_data.get('genders'),
    #                                              educations=validated_data.get('educations'),
    #                                              marital_statuses=validated_data.get('marital_statuses'),
    #                                              min_age=validated_data.get('min_age'),
    #                                              max_age=validated_data.get('max_age'))
    #
    #     locations = [CityModel.objects.filter(**location) for location in
    #                  validated_data.get('locations')]
    #     for location in locations:
    #         ad_target.locations.add(location[0])
    #
    #     languages = [LanguageModel.objects.filter(**language) for language in
    #                  validated_data.get('languages')]
    #     for language in languages:
    #         ad_target.languages.add(language[0])
    #
    #     return ad_target
    #
    # class Meta:
    #     model = AdTargetModel
    #     fields = ('id', 'ad', 'locations', 'genders', 'languages', 'educations', 'marital_statuses', 'min_age',
    #               'max_age')