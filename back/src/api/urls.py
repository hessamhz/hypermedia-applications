from django.urls import include, path
from src.api.views import (
    ContactUsCreateView,
    MemberAvatarListView,
    MemberDetailView,
    MemberListView,
    ProjectDetailView,
    ProjectListView,
    ServiceDetailView,
    ServiceListView,
)

v_1_url_patterns = [
    path("members/", MemberListView.as_view(), name="member-list"),
    path("members/avatars/", MemberAvatarListView.as_view(), name="member-avatars"),
    path("members/<slug:slug>/", MemberDetailView.as_view(), name="member-detail"),
    path("projects/", ProjectListView.as_view(), name="project-list"),
    path("projects/<slug:slug>/", ProjectDetailView.as_view(), name="project-detail"),
    path("services/", ServiceListView.as_view(), name="service-list"),
    path("services/<slug:slug>/", ServiceDetailView.as_view(), name="service-detail"),
    path("contact-us/", ContactUsCreateView.as_view(), name="contact-us-create"),
    path("tinymce/", include("tinymce.urls")),
]


urlpatterns = [
    path("v1/", include(v_1_url_patterns)),
]
