from django.urls import path, include
from .views import *
from rest_framework import routers

app_name = "api"

router = routers.SimpleRouter()
router.register('todo/', TodoViewSet, basename="todo")
router.register('users/', UserViewSet, basename="users")
urlpatterns = [
    path('',include(router.urls)),
]