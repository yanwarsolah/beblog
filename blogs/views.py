from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

from blogs.forms import CommentForm
from blogs.models import Post, Category


def post_list(request):
    posts = Post.objects.all().order_by('-id')
    page = request.GET.get('page', 1)

    paginator = Paginator(posts, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts
    }
    return render(request, 'blogs/post_list.html', context=context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            data = form.save(commit=False)
            data.post = post
            data.save()

    else:
        form = CommentForm()

    context = {
        'post': post,
        'form': form
    }

    return render(request, 'blogs/post_detail.html', context=context)


def post_filter(request, post_filter):
    category = get_object_or_404(Category, pk=post_filter)
    posts = Post.objects.filter(category=category).order_by('-created')
    context = {
        'category': category,
        'posts': posts
    }
    return render(request, 'blogs/post_filter.html', context=context)