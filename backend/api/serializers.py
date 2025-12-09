from rest_framework import serializers
from .models import Portfolio, Contact, Team, Client, Student, Book, Author, CustomUser
from django.contrib.auth import authenticate

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            'id', 'username', 'email',
            'first_name', 'last_name', 'phone_number', 'role', 'date_joined', 'created_at', 'updated_at'
        )
        read_only_fields = ('id', 'date_joined', 'created_at', 'updated_at')

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, min_length=8)
    password1 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'password1', 'role')

    def validate(self, attributes):
        if attributes['password'] != attributes['password1']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attributes
    
    def email_validation(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email is already in use.")
        return value
    
    def create(self, validated_data):
        validated_data.pop('password1')
        user = CustomUser.objects.create_user(**validated_data)
        return user

class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise serializers.ValidationError("Invalid username or password.")
        else:
            raise serializers.ValidationError("Both username and password are required.")
        attrs['user'] = user
        return attrs
    class Meta:
        model = CustomUser
        fields = ('username', 'password')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = '__all__'

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'  

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'  