from rest_framework import serializers
from .models import Leads, TutorInformation
from tutors.models import Tutors


class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutors
        fields = ('id', 'first_name', 'last_name',
                  'email', 'phone_number', 'profiles')


class TutorInformationSerializer(serializers.ModelSerializer):
    tutor = TutorSerializer()  # Nested Serializer for Tutor

    class Meta:
        model = TutorInformation
        fields = ('id', 'apply_status', 'preferred_rate',
                  'remarks', 'timings', 'tutor')


class TutorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TutorInformation
        fields = '__all__'


class LeadSerializer(serializers.ModelSerializer):

    tutors = TutorInformationSerializer(many=True)

    class Meta:
        model = Leads
        fields = ('id', 'code', 'description', 'client_name', 'client_number',
                  'remarks', 'many_tutor_link', 'status', 'created_date', 'last_reviewed_date', 'tutors')


class LeadCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leads
        fields = ('code', 'description', 'client_name', 'client_number',
                  'remarks', 'many_tutor_link')


class LeadUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leads
        fields = ('code', 'description', 'client_name', 'client_number',
                  'remarks', 'many_tutor_link', 'status', 'last_reviewed_date')
        extra_kwargs = {
            'code': {'required': False},
            'description': {'required': False},
            'client_name': {'required': False},
            'client_number': {'required': False},
            'remarks': {'required': False},
            'many_tutor_link': {'required': False},
            'status': {'required': False},
            'new_applications': {'required': False},
            'sent_applications': {'required': False},
            'pending_applications': {'required': False},
            'last_reviewed_date': {'required': False},
            'tutors': {'required': False}
        }
