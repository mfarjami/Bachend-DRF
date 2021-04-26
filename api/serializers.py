from .models import Todo
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueTogetherValidator

class TodoSerializer(serializers.ModelSerializer):
    author =  serializers.HiddenField(default=serializers.CurrentUserDefault())
    def get_user(Self, obj):
            return {
                obj.author.username
            }
    user = serializers.SerializerMethodField("get_user")
    # author = serializers.DateTimeField(
    #     default=serializers.CreateOnlyDefault(timezone.now)
    #     )
    
    class Meta:
        model = Todo
        fields = "__all__"
        # exclude = ['author']

       
       
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"