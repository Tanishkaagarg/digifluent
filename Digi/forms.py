from django import forms

class Contact(forms.Form):
    name = forms.CharField( required=True)
    
    email = forms.EmailField(required=True)
    
    message = forms.CharField(widget=forms.Textarea, required=True)