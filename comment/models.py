from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Comments(models.Model):
    user_name = models.CharField(max_length=255)
    mail = models.EmailField(max_length=255)
    home_page = models.URLField(max_length=255, blank=True, null=True)
    text = models.TextField()
    modified = models.TimeField(auto_now_add=True)
    parent = TreeForeignKey("Comments", on_delete=models.CASCADE,
                            null=True, blank=True, related_name="children")

    class MPTTMeta:
        order_insertion_by = ["modified"]

    def __str__(self):
        return self.text
