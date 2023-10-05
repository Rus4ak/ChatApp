from django.urls import path, include
from . import views

urlpatterns = [
    path('auth/', include('rest_framework.urls')),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('profiles/', views.ProfileList.as_view()),
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('chats/', views.ChatList.as_view()),
    path('chats/<int:pk>/', views.ChatDetail.as_view())
]
