from django.urls import path
from .views import TopicView, CommentView, RepliesView, TopicApiView, CommentApiView, RepliesApiView
urlpatterns = [

    path('api/topics/', TopicApiView.as_view(), name='api_topic_list'),
    path('api/topics/<int:pk>/', TopicApiView.as_view(), name='api_topic_detail'),
    path('api/comments/<int:topic_pk>/', CommentApiView.as_view(), name='api_comment_list'),
    path('api/comments/<int:topic_pk>/<int:pk>/', CommentApiView.as_view(), name='api_comment_detail'),
    path('api/replies/<int:comment_pk>/', RepliesApiView.as_view(), name='api_replies_list'),
    path('api/replies/<int:comment_pk>/<int:pk>/', RepliesApiView.as_view(), name='api_replies_detail'),
    path('' , TopicView.as_view(), name='topic_list'),
    path('comments/<int:topic_id>/', CommentView.as_view(), name='comment_list'),
    path('replies/<int:comment_id>/', RepliesView.as_view(), name='replies_list'),
]
