from rest_framework import generics
from models import Post,Author
from serializers import PostSerializer, AuthorSerializer
# Create your views here.


class PostList(generics.ListCreateAPIView):
    """
    List and create Posts
    """
    queryset=Post.objects.all()
    serializer_class=PostSerializer


class PostDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Gets a detailed view of an individual post record. Can be updated
    and deleted. Each post must
    be assigned to a author
    """
    queryset=Post.objects.all()
    serializer_class=PostSerializer

class AuthorList(generics.ListCreateAPIView):
    """
    List and create Posts
    """

    queryset=Author.objects.all()
    serializer_class=AuthorSerializer


class AuthorDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Returns the details on an author
    """
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer
