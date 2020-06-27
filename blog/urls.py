from django.urls import path

from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView
)


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostUpdateView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostDetailView.as_view(), name='post-update'),
]
