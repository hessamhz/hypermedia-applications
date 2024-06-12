from django.urls import include, path

v_1_url_patterns = []

urlpatterns = [
    path("v1/", include(v_1_url_patterns)),
]
