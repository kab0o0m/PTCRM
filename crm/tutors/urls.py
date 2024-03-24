from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = "tutors"

urlpatterns = [
    path("", views.TutorListView.as_view(), name="tutor-list"),
    path("<int:pk>/", views.TutorRetrieveUpdateDestroy.as_view(), name="tutor-update"),
    path('<int:pk>/add_profile/',
         views.AddProfileToTutor.as_view(), name='add_profile_to_tutor'),
    path("view/", views.tutor_list, name="tutor-view"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
