from django.urls import path
from .views import comments_list_view

app_name = "blog"

urlpatterns = [
    path("", comments_list_view, name="comment-list"),
]
