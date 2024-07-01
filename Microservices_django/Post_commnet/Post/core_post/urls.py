from django.urls import path
from core_post.views import PostApiView, PostCommentApiViewPost

urlpatterns = [
    path('posts/', PostApiView.as_view(), name="api_post_home"),
    # path('posts/<int:id>/', PostApiView.as_view(), name="api_post_home"),
    path('posts/<str:id>/comments', PostCommentApiViewPost.as_view()),
]