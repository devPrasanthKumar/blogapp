# from django.shortcuts import get_object_or_404
# from myblogapp.models import BlogCategory, BlogUploader


# def category_wise_context(request):
#     # Assuming you have a default category or handle the case when no category is provided
#     slug = 'default-category'
#     if 'category_slug' in request.GET:
#         slug = request.GET['category_slug']

#     get_slug = get_object_or_404(BlogCategory, slug=slug)
#     dbname = BlogUploader.objects.filter(category=get_slug)

#     context = {
#         "catwise": dbname,
#     }
#     return context
