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


class UpdatePortfolioForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = ('name', 'description', 'categories', 'thumbnail',)

    # def save(self, commit=True):
    #     user = super(UpdatePortfolioForm, self).save(commit=False)
    #     user.name = self.cleaned_data['name']
    #     user.description = self.cleaned_data['description']
    #     user.categories = self.cleaned_data['categories']
    #     if commit:
    #         user.save()

