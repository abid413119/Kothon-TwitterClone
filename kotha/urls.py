from django.urls import path
from django.conf.urls import url
from django.views.generic.base import RedirectView
from .views import KothaCreateView, KothaListView, KothaDetailView, KothaUpdateView, KothaDeleteView

app_name = "kotha"

urlpatterns = [
    url(r'^$', RedirectView.as_view(url="/")),
    url(r'^search/$', KothaListView.as_view(), name="kotha-list"),
    url(r'^create/$', KothaCreateView.as_view(), name="kotha-create"),
    url(r'^(?P<pk>\d+)/$', KothaDetailView.as_view(), name="kotha-detail"),
    url(r'^(?P<pk>\d+)/update/$', KothaUpdateView.as_view(), name="kotha-update"),
    url(r'^(?P<pk>\d+)/delete/$', KothaDeleteView.as_view(), name="kotha-delete"),
]
