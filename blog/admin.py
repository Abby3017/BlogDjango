from django.contrib import admin
from .models import Blog,Blogger,Comment,Topic
# Register your models here.

admin.site.register(Blog)
admin.site.register(Blogger)
admin.site.register(Comment)
admin.site.register(Topic)