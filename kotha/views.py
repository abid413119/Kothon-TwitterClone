from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Kotha


# Class Based View

class Kotha_list(ListView):
    model = Kotha
    context_object_name = 'all_kotha_list'

class Kotha_detail(DetailView):
    model = Kotha



# Function Based View

# def kotha_list_view(request):
#     all_objects = Kotha.objects.all()
#     context = {
#         "object_list": all_objects,
#     }
#     return render(request, "kotha/list_view.html", context)


# def kotha_detail_view(request, id=1):
#     obj = Kotha.objects.get(id=id)
#     context = {
#         "object": obj,
#     }
#     return render(request, "kotha/detail_view.html", context)


