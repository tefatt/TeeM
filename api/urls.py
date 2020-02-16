from django.urls import re_path, include
from rest_framework.urlpatterns import format_suffix_patterns

from api.views import *

urlpatterns = format_suffix_patterns([
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # re_path(r'^oauth/', include('rest_framework_social_oauth2.urls')),
    re_path(r'^login/$', ObtainToken.as_view()),
    re_path(r'^users/$', UserListCreate.as_view(), name='user-list-create'),
    re_path(r'^exercise/$', ExerciseListCreate.as_view(), name='exercise-list-create')
])
