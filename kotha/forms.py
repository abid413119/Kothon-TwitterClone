from django import forms
from .models import Kotha


class KothaModelForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(attrs={'placeholder': "Your Message", "class":"form-control", 'rows':3, 'cols':10}))
    class Meta:
        model = Kotha
        fields = [
            'content',
        ]
    
    # def clean_content(self, *args, **kwargs):
    #     content = self.cleaned_data['content']
    #     if content == 'abc':
    #         raise forms.ValidationError("Can't be abc")
    #     return content

