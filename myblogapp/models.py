from django.db import models
from django.utils import timezone
from authUser.models import CustomUser
from django.utils.text import slugify
from django.urls import reverse
import os
import uuid

from ckeditor_uploader.fields import RichTextUploadingField


class BlogCategory(models.Model):
    # Other fields for your model

    category = models.CharField(max_length=400)
    slug = models.SlugField(max_length=200, default="others")

    def __str__(self):
        return self.category


class BlogUploader(models.Model):
    title = models.CharField(max_length=400)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, default=None)
    description = RichTextUploadingField()
    image = models.ImageField(upload_to="uploads/",
                              default=None, null=True, blank=True)
    upload_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            super().save(*args, **kwargs)


class BlogComment(models.Model):
    comment = models.TextField()
    commentUser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    commentPost = models.ForeignKey(
        BlogUploader, on_delete=models.CASCADE, default=None, null=True, blank=True)

    def __str__(self):
        return self.comment
