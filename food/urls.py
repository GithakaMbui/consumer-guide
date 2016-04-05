from django.conf.urls import include, url
from . import views
from django.conf import settings

urlpatterns = [url(r'^food/item_list/$', views.item_list, name='item_list'),
url(r'^post/new/$', views.post_edit, name='post_edit'),
url(r'^food/index/$', views.index, name='index'),
url(r'^food/$', views.home, name='home'),
url(r'^food/register/$', views.register, name='register'),
url(r'^food/login/$',views.user_login, name='login'),
url(r'^food/user_logout/$', views.user_logout, name='logout'),
url(r'^food/add_product/$', views.add_product, name='add_product'),
url(r'^food/food_list/$', views.food_list, name='food_list'),
url(r'^food/forex/$', views.forex, name='forex'),
url(r'^food/forex_rates/$', views.forex_rates, name='forex_rates'),
url(r'^food/forexby_bureau/$', views.forexby_bureau, name='forexby_bureau'),
url(r'^food/loans/$', views.loans, name='loans'),
url(r'^food/table_view/$', views.table_view, name='table_view'),
url(r'^food/price_comparison/$', views.price_comparison, name='price_comparison'),
url(r'^food/forex_comparison/$', views.forex_comparison, name='forex_comparison'),
url(r'^food/loan_comparison/$', views.loan_comparison, name='loan_comparison'),
url(r'^food/cart_comparison/$', views.cart_comparison, name='cart_comparison'),

url(r'^static/(?P<path>.*)$',
        'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
]