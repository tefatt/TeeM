from rest_framework import serializers
from api.models.institution import InstitutionModel

class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstitutionModel
        field = ('name', 'address', 'city', 'web_address', 'facebook','info')

    def create(self, validated_data):
        return InstitutionModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.city = validated_data.get('city', instance.city)
        instance.web_address = validated_data.get('web_address', instance.web_address)
        instance.facebook = validated_data.get('facebook', instance.facebook)
        instance.info = validated_data.get('info', instance.info)
        return instance

