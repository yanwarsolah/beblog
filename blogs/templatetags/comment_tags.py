from django import template
from django.db.models import Count

from blogs.models import Category, Comment

register = template.Library()

@register.inclusion_tag('components/list_comment.html')
def list_comment(post):
    comments = Comment.objects.filter(post=post).order_by('-created')
    return {'comments': comments}
