from django.urls import path
from . import views

urlpatterns = [
    path("feed/", views.feed, name="feed"),
    path("create/", views.create_post, name="create_post"),
    path("like/<int:post_id>/", views.like_post, name="like_post"),
    path("comment/<int:post_id>/", views.add_comment, name="add_comment"),
    path('follow/<int:user_id>/', views.follow_user, name='follow'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('myprofile/', views.my_profile, name='my_profile'),
    path('profile/', views.my_profile),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    
]