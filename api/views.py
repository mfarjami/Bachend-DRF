from .models import Todo
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from .serializers import TodoSerializer, UserSerializer
from .permissions import IsSuperUser, IsAuthorOrReadOnly
from rest_framework.viewsets import ModelViewSet


# Create your views here.

class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all()  
    serializer_class = TodoSerializer
    filterset_fields = ['completed',]
    search_fields = ['title']
    ordering_fields = ["created","completed"]
    ordering = ["-created"]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Todo.objects.all()
        return Todo.objects.filter(author=self.request.user)


    def get_permissions(self):
        if self.action in ['list','create']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthorOrReadOnly]
        return [permission() for permission in permission_classes]
    

# class TodoList(ListCreateAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer
#     # permission_classes = (IsAuthorUser,)

# class TodoDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer
#     permission_classes = (IsAuthorOrReadOnly,)

class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUser,)


