from django.shortcuts import render
from .models import Tutors
from .serializers import TutorSerializer, TutorCreateSerializer, TutorsUpdateSerializer, ProfileCreateSerializer
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
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


class AddProfileToTutor(APIView):
    def post(self, request, pk):
        try:
            tutor = Tutors.objects.get(pk=pk)

        except Tutors.DoesNotExist:
            return Response({"error": "Tutor not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProfileCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(tutor=tutor)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def tutor_list(request):
    tutors = Tutors.objects.all()
    return render(request, 'tutors/tutors-list.html', {'tutors': tutors})
