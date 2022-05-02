from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('view-posts/', views.view_posts, name="view-posts"),
    path('view-posts/<int:pk>/', views.view_posts_detail, name="view-posts-detail"),
    path('view-posts/<int:pk>/update/', views.view_posts_update, name="view-posts-update"),
    path('view-posts/create-new-post/', views.CreateNewPost, name="create-new-post"),
    path('view-posts/<int:pk>/delete/', views.view_posts_delete, name="view-posts-delete"),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('register/', views.Register, name='register'),

    # search
    path('search/', views.Search, name='search'),
]
