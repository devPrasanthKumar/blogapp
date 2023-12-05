from django import forms
from .models import BlogUploader, BlogCategory, BlogComment
from ckeditor_uploader.widgets import CKEditorUploadingWidget
import bleach


class PostForm(forms.ModelForm):

    class Meta:
        model = BlogUploader
        fields = '__all__'
        exclude = ["slug", "author", "views"]

    description = forms.CharField(widget=CKEditorUploadingWidget())

    def clean_description(self):
        html_content = self.cleaned_data['description']
        plain_text = bleach.clean(html_content, tags=[], strip=True)
        return plain_text


class CatFor(forms.ModelForm):
    class Meta:
        model = BlogCategory
        fields = "__all__"


class CommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ("comment",)
