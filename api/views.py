import datetime
import pytz
from django.utils import timezone
from dateutil import tz

from django.shortcuts import get_object_or_404
from django.db.models import Q, Count, F, Case, When, IntegerField, Max, Sum, Avg, Prefetch
from rest_framework import status, parsers, renderers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, CreateAPIView, \
    RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView

from api.models import *
from api.serializers import *
from api.user_helpers import UserHelpers


class ObtainToken(APIView):
    """
    View to get authentication token (login).
    """
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    def post(self, request):
        """
        Send user's credentials to obtain auth token.
        :param request: request object.
        :return: user data.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        user.last_login = timezone.now()
        user.save()
        token, created = Token.objects.get_or_create(user=user)
        role = UserHelpers.get_user_role(user)
        return Response({'token': token.key,
                         'username': user.username,
                         'role': role,
                         'user_id': user.id,
                         'first_name': user.first_name,
                         'last_name': user.last_name,
                         'email': user.email})


class UserListCreate(ListCreateAPIView):
    """
    API for retrieving list of users (GET) and creating new ones (POST)
    """
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        queryset = UserModel.objects.all()
        user_id = self.request.query_params.get('id')
        if user_id:
            queryset = queryset.filter(id=user_id)
        return queryset


class ExerciseListCreate(ListCreateAPIView):
    queryset = ExerciseModel.objects.all()
    serializer_class = ExerciseSerializer

    # permission_classes = [IsAdminUser]

    def create(self, request, *args, **kwargs):
        try:
            serializer = ExerciseSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            raise ex


class ExerciseRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    """
    API for retrieving, updating and deleting of a exercise (GET, PUT and DELETE)
    """
    permission_classes = [IsAuthenticated, ]

    def retrieve(self, request, pk=None, **kwargs):
        """
        Retrieve a exercise instance.
        :param request: request object.
        :param pk: primary key.
        :param kwargs: keywords arguments.
        :return: exercise instance.
        """
        queryset = ExerciseModel.objects.all()
        campaign = get_object_or_404(queryset, pk=pk)
        serializer = CampaignSerializer(campaign)
        return Response(serializer.data)

    def update(self, request, pk=None, **kwargs):
        """
        Update existing exercise.
        :param request: request object.
        :param pk: primary key.
        :param kwargs: keywords arguments.
        :return: Updated instance of the exercise.
        """

        campaign = CampaignModel.objects.get(pk=pk)

        serializer = Ca(campaign, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def destroy(self, request, pk=None, **kwargs):
        """
        Delete a exercise instance.
        :param request: request object.
        :param pk: primary key.
        :param kwargs: keyword arguments.
        :return: HTTP 204 or HTTP 404.
        """

        campaign = CampaignModel.objects.get(pk=pk)
        campaign.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
