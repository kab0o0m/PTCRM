from django.shortcuts import render
from .models import Tutors
from .serializers import TutorSerializer, TutorCreateSerializer, TutorsUpdateSerializer
from rest_framework import generics
# Create your views here.


class TutorListView(generics.ListCreateAPIView):
    queryset = Tutors.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return TutorCreateSerializer
        return TutorSerializer


class TutorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tutors.objects.all()
    serializer_class = TutorsUpdateSerializer
    lookup_field = "pk"
