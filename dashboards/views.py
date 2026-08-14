from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from blogs.models import Blog, Category

# Create your views here.

@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count()
    blogs_count = Blog.objects.all().count()
    
    context = {
        'category_count':category_count,
        'blogs_count':blogs_count
    }
    return render(request,'dashboards/dashboard.html', context)

