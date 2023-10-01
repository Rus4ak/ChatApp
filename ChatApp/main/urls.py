from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('chat/<int:user_id>/', views.chat, name='chat')
]
