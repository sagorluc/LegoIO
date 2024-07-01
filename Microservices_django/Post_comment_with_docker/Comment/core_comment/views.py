from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from core_comment.models import Comment
from core_comment.serializers import CommentSerializer
import requests
import random
# Create your views here.

class PostCommentApiViewComment(APIView):
    def get(self, request, id=None):
        comments = Comment.objects.filter(post_id=id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
        
    

class CommentApiView(APIView):  
    def get(self, request, id=None):
        if id is not None:
            try:
                post = Comment.objects.get(pk=id)
                serializer = CommentSerializer(post)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Comment.DoesNotExist:
                return Response({"error": "Comment not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            posts = Comment.objects.all()
            serializer = CommentSerializer(posts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
     
    def post(self, request):
        data = request.data
        serializer = CommentSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        # Comment post
        comment = serializer.data
        print(comment, 'line 43 comment')
        
        if random.randint(1, 10) <= 9: # 10% failed
            # request to post project microservices by endpoint
            req = requests.post('http://127.0.0.1:8000/api/posts/%d/comments' % comment['post_id'], json={
                'text': comment['text']
            })
            print(req, 'line 47 comment')
            if not req.ok:
                print(req, 'line 50')
                pass
        
        return Response(comment, status=status.HTTP_201_CREATED)
