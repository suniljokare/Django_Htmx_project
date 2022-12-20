from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *



class DateInput(forms.DateInput):
    input_type = 'date'


class ExpenseForm(forms.ModelForm):
    date = forms.DateTimeField(widget=
                                forms.widgets.DateTimeInput
                                (format='%Y-%m-%d %H:%M', 
                                attrs={'class':'myDateClass', 'type':'datetime-local'}))

    class Meta:
        model = Expense 
        fields =('date','ename','eamount','pay_mode','expense_type')
        widgets = {
            'date': DateInput(),
        }
        


class RegisterForm(UserCreationForm):
   
    class Meta:
       model = User
       fields = ["username", "email", "password1", "password2"]


    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            print(email, '***********************')
            raise forms.ValidationError("Email is not unique")
        return email

    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     (first, second,) = email.split("@")
    #     (domain, exn,) = second.split(".")
    #     if domain != "tmail":
    #         raise forms.ValidationError("Domain must be 'tmail'")
        
    #     if User.objects.filter(email=email).exists():
    #         print('######################')
    #         raise forms.ValidationError("Email is alreday registered ")

    #     return email 


    # def save(self, commit=True):
    #     user = super(RegisterForm, self).save(commit=False)
    #     user.fullname = self.cleaned_data["fullname"]
    #     user.email = self.cleaned_data["email"]
    #     if commit:
    #         user.save()
    #     return user




