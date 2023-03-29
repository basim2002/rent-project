from django import forms
from django.contrib.auth.forms import UserCreationForm

from basim.models import District, Area, Book, Login, Book_Category, Feedback


class Customer_form(UserCreationForm):
    date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model=Login
        fields=['username','password1','password2','name','email','phone_no','image']

class Dealer_form(UserCreationForm):

    class Meta:
        model=Login
        fields=['username','password1','password2','name','email','phone_no','image']

class Districtform(forms.ModelForm):
    class Meta:
        model=District
        fields="__all__"

class Areaform(forms.ModelForm):
    class Meta:
        model=Area
        fields=('district_name','area_name')

class Bookform(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model=Book
        fields=['book_name','prize','author','date','image']

class Book_category_form(forms.ModelForm):
    class Meta:
        model=Book_Category
        fields=['category_name']

class Feedback_form(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model=Feedback
        fields=['feedback','date']

class Replay_form(forms.ModelForm):
    class Meta:
        model=Feedback
        fields=['replay']






