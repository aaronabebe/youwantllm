# forms.py

from django import forms


class EmailSignupForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'p-2 border-gray-300 rounded-lg', 'placeholder': 'Your email'}), label='')
