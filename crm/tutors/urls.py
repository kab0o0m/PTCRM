from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views


app_name = "tutors"

urlpatterns = [
    path("", login_required(views.TutorListView.as_view()), name="tutor-list"),
    path("<int:pk>/", views.TutorRetrieveUpdateDestroy.as_view(), name="tutor-update"),
    path('<int:pk>/add_profile/',
         views.AddProfileToTutor.as_view(), name='add_profile_to_tutor'),
    path("view/", views.tutor_list, name="tutor-view"),

]
