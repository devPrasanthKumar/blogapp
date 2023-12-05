from django.urls import path
from . import views

urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("upload-data", views.UploadData.as_view(), name="upload"),
    path("single-post-view/<str:slug>",
         views.OneView.as_view(), name="single-post-view"),
    # path("category/<int:pk>", views.CategoryWise.as_view(), name="categoryewise")
    path("category/<str:slug>", views.CategoryWise, name="categoryewise"),
    # path("sample/<int:pk>", views.sample.as_view(), name="sample"),
    path("sample/<int:pk>", views.sample, name="sample"),
    path("du", views.Dummy.as_view(), name="dum")
]
