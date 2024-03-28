from django.urls import path
from . import views

app_name = "leads"

urlpatterns = [
    path("", views.LeadListView.as_view(), name="lead-list"),
    path("<int:pk>/", views.LeadRetrieveUpdateDestroy.as_view(), name="lead-update"),
    path('tutor-information/', views.TutorInformationAPIView.as_view(),
         name='tutor-information-list'),
    path('tutor-information/<int:lead_id>/', views.TutorInformationDetailView.as_view(),
         name='tutor-information-detail'),
    path("view/", views.lead_list, name="view-list")

]
