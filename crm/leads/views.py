from django.shortcuts import render
from rest_framework import generics
from .models import Leads
from .serializers import LeadSerializer, LeadCreateSerializer, LeadUpdateSerializer


class LeadListView(generics.ListCreateAPIView):
    queryset = Leads.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return LeadCreateSerializer
        return LeadSerializer


class LeadRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Leads.objects.all()
    serializer_class = LeadUpdateSerializer
    lookup_field = "pk"
