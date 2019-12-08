from django import template
from blog.models import Post


register = template.Library()


@register.simple_tag
def total_count():
    post = Post.objects.all()
    return post.count()


@register.inclusion_tag('side_post.html')
def latest_post(postal):
    posts = Post.objects.filter(tags__name__contains='Travel')
    return {'posts': posts}






