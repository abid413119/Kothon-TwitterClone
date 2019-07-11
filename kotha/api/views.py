from rest_framework import generics
from .serializers import KothaModelSerializer
from kotha.models import Kotha
from django.db.models import Q
from django.urls import reverse_lazy
from rest_framework import permissions
from .pagination import StandardResultsPagination


class KothaCreateAPIView(generics.CreateAPIView):
    serializer_class = KothaModelSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Kotha.objects.all().order_by('-updated')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class KothaListAPIView(generics.ListAPIView):
    serializer_class = KothaModelSerializer
    pagination_class = StandardResultsPagination

    def get_queryset(self, *args, **kwargs):
        im_following = self.request.user.profile.get_following()
        qs1 = Kotha.objects.filter(user__in=im_following)
        qs2 = Kotha.objects.filter(user=self.request.user)
        qs = ( qs1 | qs2 ).distinct().order_by('-updated')
        query = self.request.GET.get("q", None)
        print(self.request.GET)
        
        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
            )
            
        return qs