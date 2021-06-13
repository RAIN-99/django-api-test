from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer, VoteSerializer
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    get_object_or_404,
)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

class Post_list(ListCreateAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = Post.objects.all()
        author_name = self.request.query_params.get("author_name")

        if author_name:
            queryset = queryset.filter(author_name=author_name)

        return queryset

    def perform_create(self, serializer):
        return serializer.save()


@api_view(["PATCH"])
def vote_view(request, question_id):
    question = get_object_or_404(request, pk=question_id)
    serializer = VoteSerializer(data=request.data)
    print(question)
    if serializer.is_valid():
        choice = get_object_or_404(
            request, pk=serializer.validated_data["post"], question=question
        )
        choice.amount_of_upvotes += 1
        choice.save()
        return Response("Voted")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Comment_list(ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = Comment.objects.all()
        post = self.request.query_params.get("post")

        if post:
            queryset = queryset.filter(post=post)

        return queryset


class Post_detail(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class Comment_detail(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
