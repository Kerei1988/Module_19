from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post


# Create your views here.

def page(request):
    num_post = [1, 3, 5]
    posts = Post.objects.all().order_by('-create_date')
    try:
        per_page = int(request.GET.get('paginate_by'))
    except:
        per_page = 1
    page_numer = request.GET.get('page')
    paginator = Paginator(posts, per_page)
    page_obj=paginator.get_page(page_numer)
    context = {
        'page_obj': page_obj,
        'posts': posts,
        'paginate_by': per_page,
        'num_post': num_post
    }
    return render(request, 'paginator/page.html', context)
