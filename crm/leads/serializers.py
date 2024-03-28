from rest_framework import serializers
from .models import Leads, TutorInformation


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leads
        fields = ('id', 'code', 'description', 'client_name', 'client_number',
                  'remarks', 'many_tutor_link', 'status', 'created_date', 'last_reviewed_date')


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


class TutorInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TutorInformation
        fields = ['id', 'tutor', 'lead', 'status',
                  'preferred_rate', 'remarks', 'timings']
        # Assuming you don't want to allow updating the ID
        read_only_fields = ['id']

    def create(self, validated_data):
        return TutorInformation.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)

        # Only update other fields if provided in the request
        if 'preferred_rate' in validated_data:
            instance.preferred_rate = validated_data['preferred_rate']
        if 'remarks' in validated_data:
            instance.remarks = validated_data['remarks']
        if 'timings' in validated_data:
            instance.timings = validated_data['timings']
        instance.save()
        return instance
