from django import forms
#from django.contrib.auth.models import User
from .models import Application
from django.forms.widgets import DateInput

class DateInput(forms.DateInput):
    input_type = 'date'


class ApplicationForm(forms.ModelForm):




    class Meta():
        model = Application
        fields = '__all__'
        labels = {
        'status_list': 'Trials'
        }
        help_texts = {
            'status_list': '(Seperated by comma)',
        }
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'

        }


        # labels = {
        # 'protocol_number' : 'Protocol number'
        #
        # }

    #
    # def clean(self):
    #     cleaned_data = super(UserForm, self).clean()
    #     password = cleaned_data.get("password")
    #     confirm_password = cleaned_data.get("confirm_password")
    #
    #     if password != confirm_password:
    #         raise forms.ValidationError(
    #             "Password mismatch. Please try again!"
    #         )
