from django.contrib import admin
from .forms import KothaModelForm
from .models import Kotha


# Register your models here.

class KothaModelAdmin(admin.ModelAdmin):
    form = KothaModelForm
    # class Meta:
    #     model = Kotha 
    #     form = KothaModelForm

admin.site.register(Kotha, KothaModelAdmin)