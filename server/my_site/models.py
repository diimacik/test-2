from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Comment(models.Model):
    post = models.ForeignKey('my_site.NewsAdmin', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.author}"
            f"{self.text}"
            f"{self.created_date}"
        )
    

class NewsAdmin(models.Model):
    name = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    comments = models.ManyToManyField(Comment, blank=True, related_name='newsPomments')

    def __str__(self):
        return(
            f"{self.name} "
            f"{self.content} "
            f"({self.created_at:%Y-%m-%d %H:%M}): "
        )

