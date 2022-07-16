from django import forms
from .models import BlogUser
from blog.models import Post
from django.shortcuts import get_object_or_404


class NewUserForm(forms.ModelForm):
    name = forms.CharField(max_length=255, required=True, label='',
                           widget=forms.TextInput(attrs={'name': 'name', 'placeholder': 'name',
                                                         'class': 'appearance-none block w-full bg-gray-200 '
                                                                  'text-gray-700 border border-red-500 rounded py-3 '
                                                                  'px-4 mb-3 leading-tight focus:outline-none '
                                                                  'focus:bg-white'}),
                           )
    nickname = forms.CharField(max_length=255, label="", required=False,
                               widget=forms.TextInput(attrs={'name': 'nc', 'placeholder': 'Nick Name',
                                                             'class': 'appearance-none block w-full bg-gray-200 '
                                                                      'text-gray-700 border border-gray-200 rounded '
                                                                      'py-3 px-4 leading-tight focus:outline-none '
                                                                      'focus:bg-white focus:border-gray-500'})
                               )
    password = forms.CharField(label="", widget=forms.PasswordInput(
        attrs={'name': 'pw', 'placeholder': 'password',
               'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 '
                        'px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500 '
               }))

    class Meta:
        model = BlogUser
        exclude = ('join', 'posts')
        labels = {
            'image': ''
        }


class LoginForm(forms.Form):
    nickname = forms.CharField()
    password = forms.CharField()

    def check_valid(self):
        user = get_object_or_404(BlogUser, nickname=self.nickname)
        password = user.password == self.password
        return password


class NewPostForm(forms.ModelForm):
    title = forms.CharField(max_length=150, widget=forms.TextInput(
     attrs={
         "class": """leading-none w-full text-gray-50 p-3 focus:outline-none focus:border-blue-700 mt-4 border-0 
                  bg-gray-800 rounded """
     }
    ))
    main_desc = forms.CharField(widget=forms.Textarea(attrs={
        "class": "h-40 text-base leading-none text-gray-50 p-3 focus:outline-none focus:border-blue-700 mt-4 "
                 "bg-gray-800 border-0 rounded`"
    }), label="")
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={"class": """text-gray-50 p-3 focus:outline-none 
                                                                             focus:border-blue-700 mt-4 border-0 
                                                                             bg-gray-800 rounded"""})
                             )
    short_desc = forms.CharField(max_length=500, widget=forms.TextInput(
     attrs={
         "class": """leading-none text-gray-50 p-3 focus:outline-none
                  focus:border-blue-700 mt-4 border-0 bg-gray-800 rounded"""
     }
    ))

    class Meta:
        model = Post
        exclude = ('date', 'slug', 'author')
