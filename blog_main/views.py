from django.shortcuts import render
from about_social.models import About
from blogs.models import Blog, Category


def home(request):
    categories = Category.objects.all()
    featured_blogs = Blog.objects.filter(is_featured = True, status = "Published").order_by('-updated_at')
    not_featured_blogs = Blog.objects.filter(is_featured = False, status = "Published").order_by('-created_at')
    
    try:
        about = About.objects.get()
    except:
        about = None
    context = {
        'categories':categories,
        'featured_blogs':featured_blogs,
        'not_featured_blogs':not_featured_blogs,
        'about':about
    }
    return render(request, 'home.html',context)