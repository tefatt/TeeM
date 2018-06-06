from rest_framework import serializers

from api.models import UserModel


class UserSerializer(serializers.ModelSerializer):
    email = serializers.CharField(required=True)

    def create(self, validated_data):
        user = UserModel.objects.create_user(validated_data['username'], validated_data['email'],
                                             validated_data['password'])
        user.first_name = validated_data.get('first_name')
        user.last_name = validated_data.get('last_name')
        user.save()
        return user

    class Meta:
        model = UserModel
        fields = '__all__'
