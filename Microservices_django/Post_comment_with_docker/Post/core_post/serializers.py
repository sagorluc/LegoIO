from rest_framework import serializers
from core_post.models import Post
import json

class PostSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = '__all__'
        
    
    # Change the comment string to array   
    def get_comments(self, post):
        # return []
        return json.loads(post.comments) # Comment return by string to josn format