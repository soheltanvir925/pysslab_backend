from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PortfolioViewSet, ContactViewSet, TeamViewSet, ClientViewSet, 
    StudentViewSet, AuthorViewSet, BookViewSet, RegisterAPI, UserListAPI,
    LoginAPI, LogoutAPIView, RegisterAdminAPI
    )

router = DefaultRouter()
router.register(r'portfolios', PortfolioViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'students', StudentViewSet) # Registering StudentViewSet using APIView
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)
router.register(r'admin-users', RegisterAdminAPI)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('users/', UserListAPI.as_view(), name='user-list'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    
]