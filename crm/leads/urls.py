from django.urls import path
from . import views

app_name = "leads"

urlpatterns = [
    path("", views.LeadListView.as_view(), name="lead-list"),
    path("<int:pk>/", views.LeadRetrieveUpdateDestroy.as_view(), name="lead-update"),
    path('<str:code>/add_tutor/',
         views.AddTutorToLead.as_view(), name='add_tutor_to_lead'),
    path("view/", views.lead_list, name="view-list")

]
