from django.contrib.auth import get_user_model
from rest_framework import generics  
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny 

User = get_user_model()  


# Create your views here.
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]