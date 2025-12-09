from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import (
    Portfolio, Contact, Team, Client, Student, Author, Book, CustomUser
    )
from .serializers import (
    PortfolioSerializer, ContactSerializer, TeamSerializer, 
    ClientSerializer, StudentSerializer, AuthorSerializer,
    BookSerializer, UserLoginSerializer, UserRegistrationSerializer, UserListSerializer,
    )
from .pagination import StudentPagination
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.tokens import RefreshToken

# new class-based view using ModelViewSet for Student
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = StudentPagination
    search_fields = ['name']
    ordering_fields = ['name']
    filterset_fields = ['age']


class RegisterAPI(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Generate JWT tokens
            refresh = RefreshToken.for_user(user)


            return Response({
                    'success': True,
                    'message': 'Registration successful',
                    'user': {
                        'id': user.id,
                        'username': user.username,
                        'email': user.email
                    },
                    'tokens': {
                        'access': str(refresh.access_token),
                        'refresh': str(refresh),
                    }
                }, status=status.HTTP_201_CREATED)
        
        return Response({
            'success': False,
            'error': 'Registration failed',
            },status=status.HTTP_400_BAD_REQUEST)
    
class LoginAPI(APIView):
    """
    Login API using APIView
    """
    authentication_classes = []
    permission_classes = []
    queryset = User.objects.all()

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.validated_data['user']
            
            # Generate JWT tokens
            refresh = RefreshToken.for_user(user)
            
            return Response(status=status.HTTP_200_OK)        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutAPIView(APIView):
    """
    Logout API using APIView
    """
    def post(self, request):
        try:
            refresh_token = request.data.get('refresh_token')
            if refresh_token:
                token = RefreshToken(refresh_token)
                token.blacklist()
                return Response({'message': 'Successfully logged out'}, status=status.HTTP_200_OK)
            return Response({'error': 'Refresh token required'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)  
class UserListAPI(APIView):
    # List all users

    #permission_classes = [IsAuthenticated]


    def get(self, request):
        try:
            users = CustomUser.objects.all()
            serializer = UserListSerializer(users, many=True)

            response_data = {
                'success': True,
                'message': 'User list fetched successfully',
                'data': serializer.data
            }
            return Response(response_data, status=status.HTTP_200_OK)      

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class RegisterAdminAPI(viewsets.ModelViewSet):
    queryset = CustomUser.objects.filter(is_staff=True)
    serializer_class = UserRegistrationSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.select_related("author")
    serializer_class = BookSerializer

class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer