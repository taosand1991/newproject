from django.shortcuts import render, get_object_or_404, redirect
from blog.forms import CommentForm, PostForm, ShareEmailForm, ContactForm
from .models import Post, Category, Comment
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, Http404


# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    template = 'blog/post_list.html'
    context = {'posts': posts,
               'categories': categories,
               }
    return render(request, template, context)


@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.blog_views = post.blog_views + 1
    post.save()
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        is_liked = True
        post.save()
    # else:
    #     is_liked = False
    is_favored = False
    if post.favorites.filter(id=request.user.id).exists():
        is_favored = True

    is_tablet = False
    if post.tablets.filter(id=request.user.id).exists():
        is_tablet = True

    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()

    template = 'blog/detail.html'
    context = {'post': post,
               'form': form,
               'is_liked': is_liked,
               'is_favored': is_favored,
               'total_likes': post.total_likes,
               'is_tablet': is_tablet,
               }
    return render(request, template, context)


@login_required
def create_post(request):
    form = PostForm(data=request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        post.tags.set(form.cleaned_data.get('tags'))
        form.save_m2m()

        messages.info(request, 'Your post has been created')
        return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_create.html', {'form': form})


@login_required
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        messages.success(request, "Your Post has been Updated")
        return redirect('post_list')

    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_create.html', {'form': form, 'post': post})


@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    messages.warning(request, 'Your post has been deleted successfully')
    return redirect('post_list')


def about(request):
    return render(request, 'blog/about.html', {})


@login_required
def comment_delete(request, pk):
    commenti = get_object_or_404(Comment, pk=pk)
    commenti.delete()
    messages.success(request, "The comment has been deleted successfully")
    return redirect('detail', commenti.post.pk)


def share_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = ShareEmailForm(request.POST or None)
    if form.is_valid():
        instance = form.cleaned_data
        subject = f"This is a post shared by {instance['name']},{instance['last_name']}"
        message = f'Read the {post.title} click on the link below \n https://http://127.0.0.1:8000/23/detail/'
        send_mail(subject=subject, message=message, from_email=settings.EMAIL_HOST_USER,
                  recipient_list=[instance['email']], fail_silently=False)
        messages.success(request, "Your Email has been sent!!")
        return redirect('detail', post.pk)
    else:
        form = ShareEmailForm()
    return render(request, 'blog/share.html', {'post': post,
                                               'form': form,
                                               })


def category_details(request, category):
    posts = Post.objects.filter(tags__name__contains=category)
    context = {'category': category,
               'posts': posts
               }
    return render(request, 'blog/category.html', context)


def search_result(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        object_list = Post.objects.filter(
            Q(title__icontains=query) | Q(categories__icontains=query))

    context = {'object_list': object_list}
    return render(request, 'blog/search_results.html', context)


def contact_us(request):
    sent = False
    if request.method == "POST":

        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            instance = contact_form.cleaned_data
            subject = f"Contact message from the {instance['name']}, {instance['email']}"
            message = instance['message']
            from_email = instance['email']
            send_mail(subject=subject, message=message, from_email=from_email,
                      recipient_list=[settings.EMAIL_HOST_USER], fail_silently=False)

            messages.success(request, 'Your message has been received. Thanks!! ')
            sent = True
            return redirect('contact')
        else:
            messages.error(request, 'There is something wrong with your form')
    else:
        contact_form = ContactForm()
        return render(request, 'blog/contact_us.html', {'contact_form': contact_form,
                                                        'sent': sent})


@login_required
def liked_post(request):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True

    context = {'post': post,
               'is_liked': is_liked,
               'total_likes': post.total_likes
               }
    if request.is_ajax():
        html = render_to_string('blog/like_section.html', context, request=request)
        return JsonResponse({'form': html})
    # else:
    #     return JsonResponse({'is_liked': is_liked})

    # post = get_object_or_404(Post, pk=pk)
    # is_liked = False
    # if post.likes.filter(id=request.user.id).exists():
    #     post.likes.remove(request.user)
    #     is_liked = True
    # else:
    #     post.likes.add(request.user)
    #     is_liked = False
    # return redirect('detail', post.pk)


def favourite(request, ):
    post = get_object_or_404(Post, id=request.POST.get('post_pk'))
    if post.favorites.filter(id=request.user.id).exists():
        is_favored = False
        post.favorites.remove(request.user)
        is_favored = False

    else:
        post.favorites.add(request.user)
        is_favored = True

    context = {
        'is_favored': is_favored,
        'post': post
    }
    if request.is_ajax():
        html = render_to_string('blog/favorite_section.html', context, request=request)
        return JsonResponse({'form': html})


def tablet_like(request, id):
    post = get_object_or_404(Post, id=id)
    if post.tablets.filter(id=request.user.id).exists():
        post.tablets.remove(request.user)
    else:
        post.tablets.add(request.user)
    return HttpResponseRedirect(post.get_absolute_url())
