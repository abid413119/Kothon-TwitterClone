from django.urls import path
from django.conf.urls import url
from .views import KothaListAPIView, KothaCreateAPIView

app_name = 'kotha'
urlpatterns = [
    # url(r'^$', RedirectView.as_view(url="/")),
    url(r'^$', KothaListAPIView.as_view(), name='kotha-api-list'), # /api/kotha
    url(r'^create/$', KothaCreateAPIView.as_view(), name='kotha-api-create'),
    # url(r'^(?P<pk>\d+)/$', KothaDetailView.as_view(), name="kotha-detail"),
    # url(r'^(?P<pk>\d+)/update/$', KothaUpdateView.as_view(), name="kotha-update"),
    # url(r'^(?P<pk>\d+)/delete/$', KothaDeleteView.as_view(), name="kotha-delete"),
]
