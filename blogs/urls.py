from django.urls import path
from .views import BlogView, AllBlogView

urlpatterns = [
    path('blogs/<int:blog_id>', AllBlogView.as_view(), name='specific_blog'),
    path('blogs', BlogView.as_view(), name='all_blog'),

]
