from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

from api.views import *

urlpatterns = format_suffix_patterns([
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^oauth/', include('rest_framework_social_oauth2.urls')),
    url(r'^login/$', ObtainToken.as_view()),
    url(r'^users/$', UserListCreate.as_view(), name='user-list-create')
])
