from django import forms
from . import models

Input_class='w-full py-4 px-6 rounded-xl border'
class NewItemForm(forms.ModelForm):
    class Meta:
        model=models.Item
        fields=('name','phone_number','address','gmail')
        widgets={

            'name':forms.TextInput(attrs={'class':Input_class}),
            'phone_number':forms.TextInput(attrs={'class':Input_class}),
            'address':forms.Textarea(attrs={'class':Input_class}),
            'gmail':forms.TextInput(attrs={'class':Input_class}),
        }
class EditItemForm(forms.ModelForm):
    class Meta:
        model=models.Item
        fields = ( 'name', 'phone_number', 'address', 'gmail')
        widgets = {
            'name': forms.TextInput(attrs={'class': Input_class}),
            'phone_number': forms.TextInput(attrs={'class': Input_class}),
            'address': forms.Textarea(attrs={'class': Input_class}),
            'gmail': forms.TextInput(attrs={'class': Input_class}),
        }