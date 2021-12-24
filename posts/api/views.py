from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet

from posts.api.permissions import IsAdminOrReadOnly
from posts.api.serializers import PostSerializer
from posts.models import Post

# -------1----------
# class PostApiView(APIView):
#     # ENDPOINT GET
#     def get(self, request):
#         # posts = Post.objects.all()
#         # post_title = [post.title for post in posts]
#         serializer = PostSerializer(Post.objects.all(),many=True)
#         return Response(status=status.HTTP_200_OK, data=posts.data)
#     # ENDPOINT POST
#     def post(self, request):
#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(status=status.HTTP_200_OK, data=serializer.data)

# ---------2-------------
# class PostViewSet(ViewSet):
#     # ENDPOINT GET
#     def list(self, request):
#         # posts = Post.objects.all()
#         # post_title = [post.title for post in posts]
#         serializer = PostSerializer(Post.objects.all(),many=True)
#         return Response(status=status.HTTP_200_OK, data=serializer.data)
#     # GET DE UN ELEMENTO (se le pasa el id en la url http://127.0.0.1:8000/api/posts/6/)
#     def retrieve(self,request, pk):
#         post = PostSerializer(Post.objects.get(pk=pk))
#         return Response(status=status.HTTP_200_OK, data=post.data)
#
#     # ENDPOINT POST
#     def create(self, request):
#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(status=status.HTTP_200_OK, data=serializer.data)

# ----------3----------BUENAAAA
class PostModelViewSet(ModelViewSet):
    # DAMOS PERMISOS AL USUARIO
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()