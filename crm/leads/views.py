from django.shortcuts import render
from rest_framework import generics
from .models import Leads, TutorInformation
from .serializers import LeadSerializer, LeadCreateSerializer, LeadUpdateSerializer, TutorCreateSerializer
import jwt
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


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


class AddTutorToLead(APIView):
    def post(self, request, pk):
        try:
            lead = Leads.objects.get(pk=pk)

        except Leads.DoesNotExist:
            return Response({"error": "Tutor not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = TutorCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(lead=lead)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
