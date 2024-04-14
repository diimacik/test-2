from django.contrib import admin
from . models import NewsAdmin, Comment

# Register your models here.
admin.site.register(NewsAdmin)
admin.site.register(Comment)