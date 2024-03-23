from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"


        widgets = {
            'eid': forms.NumberInput(attrs={'class': 'form-control'}),
            'ename': forms.TextInput(attrs={'class': 'form-control'}),
            'esal': forms.NumberInput(attrs={'class': 'form_control'}),
            'mode': forms.Select(attrs={'class': 'form-control'})
        }
