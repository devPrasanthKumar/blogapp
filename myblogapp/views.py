from typing import Any
from django.db import models
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.views import View
from .models import BlogUploader, BlogCategory, BlogComment
from .forms import CatFor, PostForm, CommentForm
# Create your views here.
from django.views.generic import FormView, CreateView, ListView, DetailView, DeleteView, TemplateView
from django.urls import reverse_lazy, reverse
from django.core.paginator import Paginator


class Index(ListView):
    template_name = "html/index.html"
    model = BlogUploader
    paginate_by = 10
    context_object_name = 'topics'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cl = BlogCategory.objects.all()
        context["cl"] = cl
        return context


class UploadData(FormView):
    template_name = "html/upload.html"
    success_url = reverse_lazy("index")
    form_class = PostForm

    def form_valid(self, form):

        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)


class OneView(DetailView, FormView):
    template_name = "html/single-post.html"
    model = BlogUploader
    context_object_name = 'onepost'
    form_class = CommentForm
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        showalldata = BlogUploader.objects.all()
        showallCategory = BlogCategory.objects.all()
        commentData = BlogComment.objects.filter(commentPost=self.object)
        print("from one view :", self.object)
        countAllComment = BlogComment.objects.filter(
            commentPost=self.object).count()
        context["showalldata"] = showalldata
        context["showallCategory"] = showallCategory
        context["countAllComment"] = countAllComment
        context["commentData"] = commentData
        return context

    def form_valid(self, form):
        post_id = self.kwargs.get('slug')
        comment_post = BlogUploader.objects.get(slug=post_id)
        # Set the commentUser to the currently logged-in user
        form.instance.commentUser = self.request.user
        form.instance.commentPost = comment_post
        form.save()  # Save the comment
        return super().form_valid(form)


def CategoryWise(request, slug):
    getSlug = get_object_or_404(BlogCategory, slug=slug)
    print(getSlug)
    dbname = BlogUploader.objects.filter(category=getSlug)
    context = {
        "catwise": dbname,
    }
    return render(request, 'html/category.html', context)


class Dummy(FormView):
    template_name = "html/dummy.html"
    form_class = PostForm
    success_url = reverse_lazy("index")
    model = BlogUploader

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
# class sample(DetailView):
#     model = BlogUploader
#     template_name = "html/sam.html"
#     context_object_name = "sam"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         pk = self.kwargs.get("pk")
#         getId = get_object_or_404(BlogCategory, category=pk)
#         # 4 = 4
#         print("pk ==", pk, ",,,     get id  === ", getId)
#         li = BlogUploader.objects.filter(category=pk)
#         context["li"] = li
#         context["getid"] = getId
#         return context


def sample(req, pk):
    getId = get_object_or_404(BlogCategory, pk=pk)
    print("pk == ", ",,,     get id  === ", getId)
    li = BlogUploader.objects.filter(category=getId)
    context = {
        'li': li,
        'getid': getId,
    }

    return render(req, "html/sam.html", context)
