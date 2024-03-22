from rest_framework import serializers
from .models import Tutors


class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutors
        fields = (
            'id', 'first_name', 'last_name', 'age', 'postal_code', 'phone_number', 'email', 'remarks', 'current_occupation', 'bio', 'profile_pic', 'certificate', 'resume', 'created_date'
        )


class TutorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutors
        fields = (
            'first_name', 'last_name', 'age', 'postal_code', 'phone_number',
            'email', 'remarks', 'current_occupation', 'bio',
            'profile_pic', 'certificate', 'resume'
        )


class TutorsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutors
        fields = (
            'first_name', 'last_name', 'age', 'postal_code', 'phone_number',
            'email', 'remarks', 'current_occupation', 'bio',
            'profile_pic', 'certificate', 'resume'
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
        'bio': {'required': False},
        'profile_pic': {'required': False},
        'certificate': {'required': False},
        'resume': {'required': False},
    }
