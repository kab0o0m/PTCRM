from rest_framework import serializers
from .models import Leads


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leads
        fields = ('id', 'code', 'description', 'client_name', 'client_number',
                  'remarks', 'many_tutor_link', 'status', 'new_applications', 'sent_applications', 'pending_applications', 'created_date', 'last_reviewed_date')


class LeadCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leads
        fields = ('code', 'description', 'client_name', 'client_number',
                  'remarks', 'many_tutor_link')


class LeadUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leads
        fields = ('code', 'description', 'client_name', 'client_number',
                  'remarks', 'many_tutor_link', 'status', 'new_applications', 'sent_applications', 'pending_applications', 'last_reviewed_date')
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
        }
