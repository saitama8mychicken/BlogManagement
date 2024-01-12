from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import logging
from .models import User

# Create your views here.

logger = logging.getLogger(__name__)


class UserRegistration(APIView):
    permission_classes = []
    authentication_classes = []

    def post(self, request):
        try:
            username = request.data.get("username")
            password = request.data.get("password")

            user, created = User.objects.get_or_create(email=request.data["email"])
            if created:
                user.username = username
                user.set_password(password)
                user.save()
                return Response("Successfully Created User", status.HTTP_200_OK)
            else:
                logger.error("Failed to create user")
                return Response("user creation failed", status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(e)
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
