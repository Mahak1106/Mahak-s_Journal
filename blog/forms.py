from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post


class RegisterForm(UserCreationForm):

    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                "class": "form-control form-control-lg"
            })


class PostForm(forms.ModelForm):

    class Meta:
        model = Post

        fields = [
            "title",
            "category",
            "image",
            "excerpt",
            "content",
            "featured",
            "published",
        ]

        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Write your journal title..."
            }),

            "category": forms.Select(attrs={
                "class": "form-select form-select-lg"
            }),

            "image": forms.ClearableFileInput(attrs={
                "class": "form-control"
            }),

            "excerpt": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": "Write a short summary..."
            }),

            "content": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 15,
                "placeholder": "Start writing your story..."
            }),
        }

        labels = {
            "title": "",
            "category": "Category",
            "image": "Cover Image",
            "excerpt": "Short Description",
            "content": "",
            "featured": "Featured Story",
            "published": "Publish Immediately",
        }