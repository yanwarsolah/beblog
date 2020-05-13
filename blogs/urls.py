from django.urls import path

from blogs.views import post_list, post_detail, post_filter

app_name = 'blogs'

urlpatterns = [
    path('', post_list, name='list'),
    path('<int:post_id>/', post_detail, name='detail'),
    path('filter/<int:post_filter>/', post_filter, name='filter'),
]
