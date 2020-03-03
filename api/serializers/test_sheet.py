from rest_framework import serializers
from api.models import TestSheetModel


class TestSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestSheetModel
        fields = ['author', 'name', 'classroom', 'difficulty', 'id']
