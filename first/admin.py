from django.contrib import admin

# Register your models here.
from first.models import blog, post

class BlogAdmin(admin.ModelAdmin):
    list_display = ('date','blog')
admin.site.register(blog)
admin.site.register(post)