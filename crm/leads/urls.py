from django.urls import path
from . import views

app_name = "leads"

urlpatterns = [
    path("", views.LeadListView.as_view(), name="lead-list"),
    path("<int:pk>/", views.LeadRetrieveUpdateDestroy.as_view(), name="lead-update")

]
