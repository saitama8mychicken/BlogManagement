from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import logging
from .models import Blog
from .utils import serialize_obj

logger = logging.getLogger(__name__)


class BlogView(APIView):
    def post(self, request):
        """
            Create a new blog post
        """
        try:
            user = request.user
            title = request.data.get("title")
            if not title:
                return Response("No Tite Defined", status=status.HTTP_400_BAD_REQUEST)
            content = request.data.get("content")
            if not content:
                return Response("No content found", status=status.HTTP_400_BAD_REQUEST)

            blog_obj = Blog.objects.create(author=user,
                                           title=title,
                                           content=content)

            return Response(serialize_obj(blog_obj), status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(e)
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        """
            Retrieve a list of all blog posts
        """
        try:
            user = request.user
            all_blogs = Blog.objects.filter(author=user)
            res = []
            for blog in all_blogs:
                res.append(serialize_obj(blog))
            return Response(res, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(e)
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


class AllBlogView(APIView):
    def get(self, request, blog_id):
        """
            Retrieve details of a specific blog post
        """
        try:
            user = request.user
            blog_obj = Blog.objects.filter(id=blog_id)
            if blog_obj:
                blog_obj = blog_obj[0]
                if blog_obj.author == user:
                    res = serialize_obj(blog_obj)
                    return Response(res, status=status.HTTP_200_OK)
                else:
                    return Response("You are not authorized to access this content", status.HTTP_401_UNAUTHORIZED)
            else:
                return Response("No Such Blog", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(e)
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, blog_id):
        """
            Update an existing blog post.
        """
        try:
            user = request.user
            blog_obj = Blog.objects.get(id=blog_id)
            if blog_obj.author == user:
                if request.data.get("title"):
                    # TODO: this is not blank
                    blog_obj.title = request.data.get("title")

                if request.data.get("content"):
                    blog_obj.content = request.data.get("content")

                blog_obj.save()
                return Response(serialize_obj(blog_obj), status=status.HTTP_200_OK)
            else:
                return Response("You are not authorized to access this content", status.HTTP_401_UNAUTHORIZED)

        except Exception as e:
            logger.error(e)
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, blog_id):
        """
            Delete a blog post
        """
        try:
            user = request.user
            blog_obj = Blog.objects.get(id=blog_id)
            if blog_obj.author == user:
                blog_obj.delete()
                return Response("Deleted", status=status.HTTP_200_OK)
            else:
                return Response("You are not authorized to access this content", status.HTTP_401_UNAUTHORIZED)

        except Exception as e:
            logger.error(e)
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
