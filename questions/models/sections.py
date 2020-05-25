from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Section(MPTTModel):
    title = models.CharField(max_length=50)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return f"{self.title}"
