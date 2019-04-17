from  django.conf.urls import  url

from . import  views

app_name = 'demo1'

urlpatterns=[
    # url('index/',views.index),
    # url('index/$',views.index),
    # url(r'index/$',views.index),
    url(r'^list/$',views.list,name='list'),
    # url(r'list/(\d+)/$',views.detail),
    url(r'^detail/(\d+)/$',views.detail,name='detail'),
    url(r'^$',views.index,name='index'),
]