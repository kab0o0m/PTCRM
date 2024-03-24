from rest_framework import serializers
from .models import Tutors, Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class TutorSerializer(serializers.ModelSerializer):

    profiles = ProfileSerializer(many=True)

    class Meta:
        model = Tutors
        fields = (
            'id', 'first_name', 'last_name', 'age', 'postal_code', 'phone_number', 'email', 'remarks', 'current_occupation', 'bio', 'profiles', 'resume', 'profile_picture', 'certificate', 'created_date'
        )


class TutorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutors
        fields = (
            'first_name', 'last_name', 'age', 'postal_code', 'phone_number',
            'email', 'remarks', 'current_occupation', 'bio', 'resume', 'profile_picture', 'certificate'
        )

    def create(self, validated_data):
        return Tutors.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get(
            'first_name', instance.first_name)
        instance.last_name = validated_data.get(
            'last_name', instance.last_name)
        instance.age = validated_data.get('age', instance.age)
        instance.postal_code = validated_data.get(
            'postal_code', instance.postal_code)
        instance.phone_number = validated_data.get(
            'phone_number', instance.phone_number)
        instance.email = validated_data.get('email', instance.email)
        instance.remarks = validated_data.get('remarks', instance.remarks)

        instance.save()
        return instance


class TutorsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutors
        fields = (
            'first_name', 'last_name', 'age', 'postal_code', 'phone_number',
            'email', 'remarks', 'current_occupation', 'bio'

        )
    extra_kwargs = {
        'first_name': {'required': False},
        'last_name': {'required': False},
        'age': {'required': False},
        'postal_code': {'required': False},
        'phone_number': {'required': False},
        'email': {'required': False},
        'remarks': {'required': False},
        'current_occupation': {'required': False},
        'bio': {'required': False}

    }
