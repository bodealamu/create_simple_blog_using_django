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


def posts_by_category(request, category_slug):
    """View that lists the posts which belong to a category."""
    list_of_posts = Post.objects.all().filter(published=True).filter(category__category_slug=category_slug)

    context = {
        "list_of_posts":list_of_posts,

    }

    return render(request=request, template_name="pages/posts_by_category.html", context=context)

