from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.Post_detail.as_view(), name='post_detail'),
    
    
]