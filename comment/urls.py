from django.urls import path
from .views import post_single

app_name = "blog"

urlpatterns = [
    path("<slug:post>/", post_single, name="post_single"),
]
