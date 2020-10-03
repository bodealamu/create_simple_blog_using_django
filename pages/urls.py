from django.urls import path, include
from pages import views

urlpatterns = [
    path('', views.home, name='home'),
    path('categories', views.list_of_categories, name='categories'),
    path('categories/<str:category_slug>', views.posts_by_category, name='postlistbycategory'),
    path('<str:blog_slug>', views.post_detail, name='post_content'),

]