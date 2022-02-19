from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home-page"),
    path("new-post/", views.new_post, name="new-post"),
    path("edit/<slug:slug>/", views.edit_post, name="edit-post"),
    path('delete/<slug:slug>/', views.delete_post, name="delete-post"),
    path("<slug:slug>/", views.post_page, name="post-details"),
]
