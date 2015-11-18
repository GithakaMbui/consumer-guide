from django.conf.urls import include, url
from . import views

urlpatterns = [url(r'^$', views.item_list, name='item_list'),
url(r'^post/new/$', views.post_edit, name='post_edit'),
]