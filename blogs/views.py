from django.shortcuts import get_object_or_404, redirect, render
from blogs.models import Blog, Category, Comment
from django.db.models import Q

# Create your views here.

def posts_by_category(request, category_id):
    posts = Blog.objects.filter(status="Published",category = category_id)
    try:
        category = Category.objects.get(id = category_id)
    except:
        return redirect('home.html')
    # category = get_object_or_404(Category,id=category_id)
    categories = Category.objects.all()
    context = {
        'posts':posts,
        'category_id':category_id,
        'category':category,
        'categories':categories
    }
    
    return render(request,'post_by_category.html',context)

def blogs(request, slug):
    single_blog = get_object_or_404(Blog,slug=slug, status="Published")
    comments = Comment.objects.filter(blog = single_blog) # Filtering out the comments related to the post
    context = {
        'single_blog':single_blog,
        'comments':comments
    }
    return render(request,'blogs.html',context)

def search(request):
    keyword = request.GET.get('keyword')
    blogs = Blog.objects.filter(Q(title__icontains = keyword) | Q(short_description__icontains = keyword) | Q(blog_body = keyword), status = "Published")
    context = {
        'blogs':blogs,
        'keyword':keyword,
    }
    return render(request, 'search.html', context)