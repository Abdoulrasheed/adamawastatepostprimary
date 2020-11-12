from . import views
from django.urls import path


urlpatterns = [
    path("", views.HomeView.as_view(),  name="home_page"),
    path("pdf_printout/<int:applicant_id>/", views.PrintoutView.as_view(), name="pdf_printout")
]
