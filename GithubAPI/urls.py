from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic.base import RedirectView

from RestAPI.views import RestApiViewSet, RestApiDestroyViewSet, RestApiActorUpdateViewSet, RestApiActorListViewSet

urlpatterns = [
    # Dummy route. Can be removed.
    url(r'^/', RedirectView.as_view(url='https://hackerrank.com', permanent=False)),
    url(r'events', RestApiViewSet.as_view(), name='list_create_event'),
    url(r'erase', RestApiDestroyViewSet.as_view(), name='erase_events'),
    url(r'actors/(?P<actor_id>[^/.]+)/', RestApiActorListViewSet.as_view(), name="list"),
    url(r'actors', RestApiActorUpdateViewSet.as_view(), name="update"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
