from django import forms 


class ContactForm(forms.Form):
    name = forms.CharField(
        label = 'Name',
        max_length=100,
        widget = forms.TextInput(attrs={
            'class': 'form-control name',
            'placeholder': 'Your name',
        })
    )
    email = forms.EmailField(
        label = 'Email',
        widget = forms.EmailInput(attrs={
            'class': 'form-control email',
            'placeholder': 'Email',
        })
    )
    subject = forms.CharField(
        label = 'Subject',
        widget = forms.TextInput(attrs={
            'class': 'form-control subject',
            'placeholder': 'Subject',
        })
    )   
    message = forms.CharField(
        label = 'Message',
        widget = forms.Textarea(attrs={
            'class': 'form-control message',
            'rows': 5,
            'placeholder': 'Enter your message',
        })
    )  