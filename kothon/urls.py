from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from  kotha.views import KothaListView
from accounts.views import UserRegisterView
from .views import home

app_name = "kothon"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('', KothaListView.as_view(), name="home"),
    path('register/', UserRegisterView.as_view(), name="register"),
    path('kotha/', include("kotha.urls", namespace='kothon-kotha')),
    path('profiles/', include("accounts.urls", namespace='kothon-profiles')),
    path('api/kotha/', include("kotha.api.urls", namespace='kotha-api')),
]


if settings.DEBUG:
    urlpatterns += (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
