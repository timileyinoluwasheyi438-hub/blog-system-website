from django.urls import path
from . import views


urlpatterns = [
    path('',views.homePageview,name="index"),
    path('all-posts/', views.allPostView, name="post") ,
    path('create-post/', views.createPostView, name="create-post"),
    path("all-posts/<int:pk>/update", views.updatePostView, name="update-post"),
    path("all-posts<int:pk>/delete", views.deletePostView, name="delete-post"),
    path("about", views.aboutPage, name="about"),
    path("advert", views.advertPage, name="advert"),
     path("contact", views.contactPage, name="contact"),
]
