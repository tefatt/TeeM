import datetime
import pytz
from django.utils import timezone
from dateutil import tz
from django.http import HttpResponse

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
from api.serializers.tutorial import TutorialSerializer
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


class TestSheetListCreateView(ListCreateAPIView):
    queryset = TestSheetModel.objects.all()
    serializer_class = TestSheetSerializer

    # permission_classes = [IsAdminUser,]

    def get(self, request, *args, **kwargs):
        qs = TestSheetModel.objects.all()
        serializer = TestSheetSerializer(qs, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        try:
            serializer = TestSheetSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            raise ex


class TestSheetRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    """
        API for retrieving, updating and deleting of a testsheet (GET, PUT and DELETE)
    """

    # permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, pk=None, **kwargs):
        qs = TestSheetModel.objects.get(id=pk)
        serializer = TestSheetSerializer(qs, many=False)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, **kwargs):
        """
        Retrieve a exercise instance.
        :param request: request object.
        :param pk: primary key.
        :param kwargs: keywords arguments.
        :return: exercise instance.
        """
        queryset = TestSheetModel.objects.all()
        exe = get_object_or_404(queryset, pk=pk)
        serializer = TestSheetSerializer(exe)
        return Response(serializer.data)

    def update(self, request, pk=None, **kwargs):
        """
        Update existing exercise.
        :param request: request object.
        :param pk: primary key.
        :param kwargs: keywords arguments.
        :return: Updated instance of the exercise.
        """

        testsheet = TestSheetModel.objects.get(pk=pk)

        serializer = TestSheetSerializer(testsheet, data=request.data)
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

        try:
            exe = TestSheetModel.objects.get(id=pk)
            exe.delete()
        except:
            return HttpResponse("COuldn't find Exe model")
        return Response(status=status.HTTP_204_NO_CONTENT)
