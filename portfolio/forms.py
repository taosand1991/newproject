from django import forms
from portfolio.models import Personal


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = ('name', 'description', 'categories', 'thumbnail', 'email')

    def save(self, commit=True):
        user = super(PortfolioForm, self).save(commit=False)
        if commit:
            user.save()

