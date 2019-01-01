from django.urls import path, include
from django.conf.urls import include, url
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name="post_new"),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path(r'^post/(?P<pk>?[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]

# http://127.0.0.1:8000/%5Epost/(%3FP7%5B0-9%5D+)/edit/$