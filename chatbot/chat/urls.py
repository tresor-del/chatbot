from django.urls import path
from .views import ChatView, chat_view

urlpatterns = [
    path('chat/', ChatView.as_view(), name='chat'),
    path('chat_view/', chat_view, name='chat_view')
   
]