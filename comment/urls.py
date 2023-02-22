from django.urls import path
from .views import post_single

app_name = "blog"

urlpatterns = [
    path("", post_single, name="post_single"),
]
