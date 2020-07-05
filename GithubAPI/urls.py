from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic.base import RedirectView

from RestAPI.views import RestApiViewSet

urlpatterns = [
    # Dummy route. Can be removed.
    url(r'^/', RedirectView.as_view(url='https://hackerrank.com', permanent=False)),
    url(r'events', RestApiViewSet.as_view(), name='list_create_event')
]

urlpatterns = format_suffix_patterns(urlpatterns)
