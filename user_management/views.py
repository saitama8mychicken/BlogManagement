from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import logging
from .models import User
import re

# Create your views here.

logger = logging.getLogger(__name__)


class UserRegistration(APIView):
    permission_classes = []
    authentication_classes = []

    def validate_email(self, email):

        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if re.fullmatch(regex, email):
            logger.debug("Email ValidATED")
            return True
        else:
            raise ValueError("Email is Incorrect")

    def post(self, request):
        try:
            username = request.data.get("username")
            password = request.data.get("password")
            email_ = request.data["email"]
            self.validate_email(email_)

            user, created = User.objects.get_or_create(email=email_)
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
