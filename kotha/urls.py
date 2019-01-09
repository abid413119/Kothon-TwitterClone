from django.urls import path
from django.conf.urls import url
from .views import  Kotha_list, Kotha_detail


# for class based view
urlpatterns = [
    url(r'^$', Kotha_list.as_view(), name='kotha-list'),
    url(r'^(?P<pk>\d+)/$', Kotha_detail.as_view(), name="kotha-detail"),
]


# urlpatterns = [
#     url(r'^$', kotha_list_view, name="kotha-list"),
#     url(r'^1/$', kotha_detail_view, name="kotha-detail")
# ]
