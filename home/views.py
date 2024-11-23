from django.shortcuts import render
from .models import Topic, Comment, Reply_to_Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView ,DeleteView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from .serializer import TopicSerializer, CommentSerializer, ReplyToCommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError

class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if not username or not password or not email:
            raise ValidationError("Username, password, and email are required.")

        if User.objects.filter(username=username).exists():
            raise ValidationError("Username already exists.")

        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)

# Create your views here.

class TopicApiView(APIView):
    def get(self, request: Request, pk=None):
        if pk:
            topic = Topic.objects.get(pk=pk)
            serializer = TopicSerializer(topic)
            return Response(serializer.data)
        topics = Topic.objects.all()
        serializer = TopicSerializer(topics, many=True)
        return Response(serializer.data)

    def post(self, request: Request):
        serializer = TopicSerializer(data=request.data,)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request: Request, pk:int):
        topic = Topic.objects.get(pk=pk)
        serializer = TopicSerializer(topic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request: Request, pk: int):
        topic = Topic.objects.get(pk=pk)
        topic.delete()
        return Response(status=204)


class CommentApiView(APIView):
    def get(self, request: Request, topic_pk: int, comment_pk=None):
        if comment_pk:
            comment = Comment.objects.get(pk=comment_pk, topic_id=topic_pk)
            serializer = CommentSerializer(comment)
            return Response(serializer.data)
        comments = Comment.objects.filter(topic_id=topic_pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request: Request, topic_pk: int):
        serializer = CommentSerializer(data=request.data, context={'topic_id': topic_pk})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request: Request, topic_pk: int, comment_pk: int):
        comment = Comment.objects.get(pk=comment_pk, topic_id=topic_pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request: Request, topic_pk: int, comment_pk: int):
        comment = Comment.objects.get(pk=comment_pk, topic_id=topic_pk)
        comment.delete()
        return Response(status=204)


class RepliesApiView(APIView):
    def get(self, request: Request, comment_pk: int, reply_pk=None):
        if reply_pk:
            reply = Reply_to_Comment.objects.get(pk=reply_pk, comment_id=comment_pk)
            serializer = ReplyToCommentSerializer(reply)
            return Response(serializer.data)
        replies = Reply_to_Comment.objects.filter(comment_id=comment_pk)
        serializer = ReplyToCommentSerializer(replies, many=True)
        return Response(serializer.data)

    def post(self, request: Request, comment_pk: int):
        serializer = ReplyToCommentSerializer(data=request.data, context={'comment_id': comment_pk})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request: Request, comment_pk: int, reply_pk: int):
        reply = Reply_to_Comment.objects.get(pk=reply_pk, comment_id=comment_pk)
        serializer = ReplyToCommentSerializer(reply, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request: Request, comment_pk: int, reply_pk: int):
        reply = Reply_to_Comment.objects.get(pk=reply_pk, comment_id=comment_pk)
        reply.delete()
        return Response(status=204)





























class TopicView(ListView):
    model = Topic
    template_name = 'home/topic_list.html'
    context_object_name = 'topics'
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['comments_count'] = Comment.objects.count()
        return context




class CommentView(ListView):
    model = Comment
    template_name = 'home/comment_list.html'
    context_object_name = 'comments'
    ordering = ['-created_at']

    def get_queryset(self):
        topic_id = self.kwargs.get('topic_id')
        comments = Comment.objects.filter(topic_id=topic_id)
        return comments

class RepliesView(ListView):
    model = Reply_to_Comment
    template_name = 'home/replies.html'
    context_object_name ='replies'
    ordering = ['-created_at']

    def get_queryset(self):
        comment_id = self.kwargs.get('comment_id')
        return Reply_to_Comment.objects.filter(comment_id=comment_id)



