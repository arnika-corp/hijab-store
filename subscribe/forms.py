from django import forms

class SubscribeForms(forms.Form):
    email = forms.EmailField(label='پست الکترونیک', max_length=100)