from django import forms

from profiles.models import UserProfileModel
from .models import Blog, BlogPost, CommentBlogPost


# Formulaires du Blog
#
# New forms.
class DesktopBlogForm(forms.ModelForm):
    theme = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'cols': 20, 'placeholder': "What's in your mind?"}
        ),
        max_length=4000,
        help_text='Create Usefull Blogs.'
    )

    class Meta:
        model = Blog
        fields = ['theme', 'illustration']

    # def __init__(self, *args, **kwargs):
    #     super(DesktopBlogForm, self).__init__(*args, **kwargs)
    #     self.fields['auteur'] = UserProfileModel.objects.first()

class DesktopPostForm(forms.ModelForm):
    # titre = forms.CharField(
    #     widget=forms.Textarea(
    #         attrs={'rows': 1, 'placeholder': "Head Lines."}
    #     ),
    # )
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'cols': 20, 'placeholder': "What's in your mind?"}
        ),
        max_length=4000,
        help_text='Post something on your Blogs.'
    )

    class Meta:
        model = BlogPost
        fields = ['titre', 'text', 'illustration', 'blog'] #

    def __init__(self, user, *args, **kwargs):
        super(DesktopPostForm, self).__init__(*args, **kwargs)
        # self.fields['blog'].queryset = Blog.objects.all()
        # self.fields['blog'].queryset = Blog.objects.filter(auteur=user.userprofilemodel)
        self.fields['blog'].queryset = Blog.objects.filter(auteur=user.profile)

class DesktopCommentForm(forms.ModelForm):
    commentaire = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'cols': 20, 'placeholder': "Leave a comment."}
        ),
        max_length=4000,
        help_text='Here You can reply to this.'
    )
    class Meta:
        model = CommentBlogPost
        fields = ['commentaire',] # 'blogpost']

    def __init__(self, post, *args, **kwargs):
        super(DesktopCommentForm, self).__init__(*args, **kwargs)
        # self.fields['blogpost'] = self.request.










# old forms.
class PostForm(forms.ModelForm):

    # text = forms.CharField(widget=forms.Textarea(attrs={'cols': 280, 'rows': 4}))

    class Meta:
        model = BlogPost

        fields = ('titre', 'text',)

        # exclude = ('illustration', 'date_post', 'slug')

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
#
#
# class PostForm(forms.Form):
#     status = forms.TextInput()


class BlogForm(forms.ModelForm):

    theme = forms.CharField(widget=forms.Textarea(attrs={'cols': 20, 'rows': 3}))
    # theme = forms.Textarea(widget=forms.TextInput(attrs={'size':3}))

    class Meta:
        model = Blog
        exclude = ('auteur', 'illustration', 'date_blog', 'slug')


class CreateBlogForm(forms.ModelForm):

    class Meta:
        model   = Blog
        fields  = ['theme',]

    def __init__(self, auteur, *args, **kwargs):
        super(CreateBlogForm, self).__init__(self, *args, **kwargs)
        self.fields['auteur'] = auteur

