from django.conf.urls import url
from django.contrib import admin

from sisdatasources.views import (
    blog,
    blog_detail
 )

urlpatterns = [
    url(r'^$', blog, name='list'),
    # url(r'^$', blog_create),
    url(r'^(?P<slug>[\w-]+)/$', blog_detail, name='detail'),
]
