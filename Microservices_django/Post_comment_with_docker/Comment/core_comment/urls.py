from django.urls import path
from core_comment.views import CommentApiView, PostCommentApiViewComment


urlpatterns = [
    path('comments/', CommentApiView.as_view()),
    path('comments/<int:id>/', CommentApiView.as_view()),
    path('comments/<str:id>/posts/', PostCommentApiViewComment.as_view()),
]
