from django import forms

from app.employee.models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = (
            'name',
            'lastname',
            'email',
            'country',
        )
