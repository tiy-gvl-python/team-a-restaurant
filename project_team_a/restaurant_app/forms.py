from __future__ import unicode_literals
from .models import Profile

from collections import OrderedDict

from django import forms


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['phone']