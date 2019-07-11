from django.db import models
from django.urls import reverse
from django.conf import settings 
from django.core.exceptions import ValidationError
from django.utils import timezone


### Validation outside the model
from .validators import validate_content

class Kotha(models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content     = models.CharField(max_length=240, validators=[validate_content])
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse("kotha:kotha-detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ['-timestamp', 'content']
    