from django.urls import path
from . import views


app_name = "tutors"

urlpatterns = [
    path("", views.TutorListView.as_view(), name="tutor-list"),
    path("<int:pk>/", views.TutorRetrieveUpdateDestroy.as_view(), name="tutor-update")

]
