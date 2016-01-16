from voter.models import Commissioner, Candidate, Voter, Category
from django.contrib.auth.models import User
from django import forms


class CommissionerForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

