from django.shortcuts import render

from blogs.models import Blog, Category


def home(request):
    categories = Category.objects.all()
    featured_blogs = Blog.objects.filter(is_featured = True, status = "Published").order_by('-updated_at')
    not_featured_blogs = Blog.objects.filter(is_featured = False, status = "Published").order_by('-created_at')
    context = {
        'categories':categories,
        'featured_blogs':featured_blogs,
        'not_featured_blogs':not_featured_blogs
    }
    return render(request, 'home.html',context)