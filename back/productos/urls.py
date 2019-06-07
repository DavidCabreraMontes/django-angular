from django.urls import path, re_path
from django.conf.urls import include
from productos import views

urlpatterns = [
    re_path(r'^$', views.productosList.as_view()),
    re_path(r'^(?P<pk>\d+)/$', views.productosList.as_view()),
    re_path(r'^view/(?P<pk>\d+)/$', views.productosOne.as_view()),
]