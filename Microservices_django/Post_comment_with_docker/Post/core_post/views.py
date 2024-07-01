from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from core_post.models import Post
from core_post.serializers import PostSerializer
import requests
import json

# Create your views here.

class PostApiView(APIView):
    def get(self, id=None):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    
    def post(self, request):
        data = request.data
        serializer = PostSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

# Make a comment of spacific post  
class PostCommentApiViewPost(APIView):
    def post(self, request, id=None):
        post = Post.objects.get(pk=id)
        
        comments = json.loads(post.comments) # This comments is an array
        print(comments, 'line 34 post') # output [{'text': 'comment 12'}]
        comments.append({
            'text': request.data['text']
        })
        print(comments, 'line 38 post') # output [{'text': 'comment 12'}, {'text': 'comment 13'}]
        post.comments = json.dumps(comments)
        post.save()
        return Response(PostSerializer(post).data)
        
        
