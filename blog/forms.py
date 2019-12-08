from django import forms
from blog.models import Comment, Post



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'content')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'tags')

    def save(self, commit=True):
        user = super(PostForm, self).save(commit=False)
        if commit:
            user.save()
        return user


class ShareEmailForm(forms.Form):
    name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=150)
    email = forms.EmailField(max_length=100)


    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email

    def clean_name(self):
        name = self.cleaned_data.get('name')
        return name
