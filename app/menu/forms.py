from django import forms
from .models import Menu
from ..lunch.models import Lunch


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = (
            'lunches',
            'published_at',
        )
        lunches = forms.ModelMultipleChoiceField(
            queryset=Lunch.objects.all(),
            widget=forms.CheckboxSelectMultiple
        )
