from django import forms

from .models import BlogPost

# Formulaires du Blog
#
class PostForm(forms.ModelForm):

    class Meta:
        model = BlogPost

        # exclude = ('illustration', 'date_post', 'slug')

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
#
#
# class PostForm(forms.Form):
#     status = forms.TextInput()
