from rest_framework import serializers
from api.models import TutorialModel


class TutorialSerializer(serializers.ModelSerializer):

    class Meta:
        model = TutorialModel
        fields = ['id', 'name', 'content', 'test_sheet_id']

        extra_kwargs = {'id': {'read_only': False},
                        'test_sheet_id': {'read_only': False}
                        }
