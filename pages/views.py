from django.shortcuts import render
from blog.models import Post


def home(request):
    """View function for home page"""
    published_posts = Post.objects.all().filter(published=True)

    context = {
        'published_posts':published_posts,
    }

    return render(request=request, template_name='pages/home.html', context=context)
