from django.urls import path
from django.conf.urls import url, include
from .views import UserDetailView, UserFollowView

app_name = "accounts"

urlpatterns = [
    
    url(r"^(?P<username>[\w,@+-]+)/$", UserDetailView.as_view(), name="user-detail"),
    url(r"^(?P<username>[\w,@+-]+)/follow/$", UserFollowView.as_view(), name="follow")
]
