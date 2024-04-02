from django.db import models


# Create your models here.
class NewsAdmin(models.Model):
    name = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return(
            f"{self.name} "
            f"{self.content} "
            f"({self.created_at:%Y-%m-%d %H:%M}): "
        )
