from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey


class Comment(MPTTModel):
    user_name = models.CharField(max_length=50)
    parent = TreeForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )
    email = models.EmailField()
    home_page = models.URLField(max_length=255, blank=True, null=True)
    text = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)

    class MPTTMeta:
        order_insertion_by = ["-publish"]

    def __str__(self):
        return self.user_name
