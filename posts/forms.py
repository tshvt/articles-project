from django import forms
from .models import Post


CHOICES = (
    (True, "Yes"),
    (False, "No")
)


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['date', 'slug']
        labels = {
            'img_url': "Image URL",
            'is_public': "Make post public?"
        }
        widgets = {
            'author': forms.TextInput(attrs={'value': '', 'id': 'author_user', 'type': 'hidden'}),
            'is_public': forms.Select(choices=CHOICES)
        }


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['date', 'slug', 'author']
        labels = {
            'img_url': "Image URL",
            'is_public': "Make post public?"
        }
        widgets = {
            'is_public': forms.Select(choices=CHOICES)
        }

