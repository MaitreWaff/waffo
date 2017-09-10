from django import forms

from .models import Blog, BlogPost

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


class BlogForm(forms.ModelForm):

    theme = forms.CharField(widget=forms.Textarea(attrs={'cols': 30, 'rows': 5}))
    # theme = forms.Textarea(widget=forms.TextInput(attrs={'size':3}))

    class Meta:
        model = Blog
        exclude = ('auteur', 'illustration', 'date_blog', 'slug')

