from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Kotha
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import FormUserNeededMixin, UserOwnerMixin
from .forms import KothaModelForm
from django.urls import reverse_lazy

# Class Based View

class KothaCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
    model = Kotha
    fields = ['content']
    template_name = "kotha/kotha_create.html"
    success_url = reverse_lazy("home")
    login_url = '/admin/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class KothaUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    model = Kotha
    # success_url = "/kotha/"
    fields = ['user', 'content']
    template_name_suffix = '_update_form'


class KothaDeleteView(LoginRequiredMixin, DeleteView):
    model = Kotha
    success_url = reverse_lazy("kothon-kotha:kotha-list")


class KothaListView(ListView):
    def get_queryset(self, *args, **kwargs):
        qs = Kotha.objects.all().order_by('-updated')
        query = self.request.GET.get("q", None)

        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
            )
            
        return qs

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context['user'] = user
        context['create_form'] = KothaModelForm()
        context['create_url'] = reverse_lazy("kothon-kotha:kotha-create")
        return context


    context_object_name = 'all_kotha_list'


class KothaDetailView(DetailView):
    model = Kotha
    
