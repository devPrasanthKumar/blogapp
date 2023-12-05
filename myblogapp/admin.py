from django.contrib import admin

# Register your models here.
from .models import BlogCategory, BlogComment, BlogUploader
# Register your models here.


admin.site.register(BlogCategory)
admin.site.register(BlogComment)


@admin.register(BlogUploader)
class AdminBlog(admin.ModelAdmin):
    list_display = ["id", "title", "category"]
