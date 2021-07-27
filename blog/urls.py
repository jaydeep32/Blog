from django.urls import path
from django.views.generic import TemplateView
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('post-detail/<str:slug>/', views.post_detail, name='post-detail'),
]


