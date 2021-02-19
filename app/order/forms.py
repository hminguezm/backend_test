from django import forms

from .models import Order
from ..menu.models import lunchesByMenu


class OrderForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.menu_id = kwargs.pop('menu_id')
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['applicant_name'] = forms.CharField(label="Name", )
        self.fields['meal'] = forms.ChoiceField(
            label="Meals",
            widget=forms.RadioSelect,
            choices=lunchesByMenu(self.menu_id),
        )
        self.fields['comment'] = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))

    def save(self):
        data = self.cleaned_data
        print(data)
        order = Order(applicant_name=data['applicant_name'], meal=data['meal'], comment=data['comment'])
        order.save()
