from django.shortcuts import render
from blog.models import Post, Category


def home(request):
    """View function for home page"""
    published_posts = Post.objects.all().filter(published=True)

    context = {
        'published_posts':published_posts,
    }

    return render(request=request, template_name='pages/home.html', context=context)


def list_of_categories(request):
    """View function for Category"""
    all_categories = Category.objects.all()

    context = {
        'all_categories' : all_categories
    }

    return  render(request=request, template_name="pages/category.html", context=context)


def test_view(request):
    return render(request=request, template_name="pages/test.html", context=None)
