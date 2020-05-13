from django import template
from django.db.models import Count

from blogs.models import Category

register = template.Library()

@register.inclusion_tag('components/card_category_filter.html')
def card_category_filter():
    categories = Category.objects.annotate(
        total_posts=Count('categories')
    )[:10]
    return {'categories': categories}
