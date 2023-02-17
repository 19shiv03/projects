from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("create/", views.AddPost.as_view()),
    path('<slug:pk>/delete/',views.DeletePost.as_view(),name="delete"),
    path('<slug:pk>/update/',views.UpdatePost.as_view(),name="update"),
    path("<slug:pk>/", views.PostDetail.as_view(), name="post_detail"),
   
]
