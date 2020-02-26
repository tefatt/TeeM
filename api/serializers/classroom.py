from rest_framework import serializers
from api.models import ClassroomModel, TeacherModel, UserModel


class ClassroomSerializer(serializers.ModelSerializer):
    #teacher = serializers.PrimaryKeyRelatedField(queryset=TeacherModel.objects.all())
    #user = serializers.PrimaryKeyRelatedField(queryset=UserModel.objects.all())

    class Meta:
        model = ClassroomModel
        fields = ('name', 'medium_language','teacher','user')
