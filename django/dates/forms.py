from django import forms
from django.forms import ModelForm


from .models import Promise


class DateInput(forms.DateInput):
    input_type = 'date'


class PromiseForm(ModelForm):

    class Meta:
        model = Promise
       # fields = ['title', 'description', 'made_on']
        fields = ['start_date','end_date']
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput(),
        }