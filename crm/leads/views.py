from django.shortcuts import render
from rest_framework import generics
from .models import Leads
from .serializers import LeadSerializer, LeadCreateSerializer, LeadUpdateSerializer
import jwt
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed


class LeadListView(generics.ListCreateAPIView):
    queryset = Leads.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return LeadCreateSerializer
        return LeadSerializer

    # Use jwt token

    def get_queryset(self):
        token = self.request.headers.get(
            'Authorization', '').split(' ')[1]
        try:
            decoded_payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            print("Token has expired.")
        except jwt.InvalidTokenError:
            print("Invalid token.")

        user_id = decoded_payload['id']
        if user_id:
            return Leads.objects.all()


class LeadRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):

    queryset = Leads.objects.all()
    serializer_class = LeadUpdateSerializer
    lookup_field = "pk"

    def get_queryset(self):
        token = self.request.headers.get('Authorization', '').split(' ')[1]
        try:
            decoded_payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            print("Token has expired.")
        except jwt.InvalidTokenError:
            print("Invalid token.")

        user_id = decoded_payload['id']
        if user_id:
            lead_id = self.kwargs.get('pk')
            return Leads.objects.all().filter(id=lead_id)


def lead_list(request):
    leads = Leads.objects.all()
    return render(request, 'leads/leads-list.html', {'leads': leads})
