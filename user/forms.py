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
    nickname = forms.CharField(label="", error_messages={
               'required': 'Please enter your nickname'
                },max_length=255,widget=
        forms.TextInput(attrs={
            "class": "w-full px-4 py-2 mt-2 border rounded-md focus:outline-none focus:ring-1 focus:ring-blue-600",
            "placeholder": "NickName"
        }))
    password = forms.CharField(label="",
                               error_messages={
               'required': 'Password is required'
                }, max_length=255,widget=forms.PasswordInput(attrs={
        "class": "w-full px-4 py-2 mt-2 border rounded-md focus:outline-none focus:ring-1 focus:ring-blue-600",
        "placeholder": "Password"
        }
    ))

    def check_valid(self, nickname, password):
        user = get_object_or_404(BlogUser, nickname=nickname)
        password = user.password == password
        return password


class NewPostForm(forms.ModelForm):
    title = forms.CharField(max_length=150,error_messages={
               'required': 'Please enter title for post'
                }, widget=forms.TextInput(
     attrs={
         "class": """leading-none w-full text-gray-50 p-3 focus:outline-none focus:border-blue-700 mt-4 border-0 
                  bg-gray-800 rounded """
     }
    ))
    main_desc = forms.CharField(error_messages={
               'required': 'You Should Have an story'
                },widget=forms.Textarea(attrs={
        "class": "h-40 text-base leading-none text-gray-50 p-3 focus:outline-none focus:border-blue-700 mt-4 "
                 "bg-gray-800 border-0 rounded`"
    }), label="")
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={"class": """text-gray-50 p-3 focus:outline-none 
                                                                             focus:border-blue-700 mt-4 border-0 
                                                                             bg-gray-800 rounded"""})
                             )
    short_desc = forms.CharField(max_length=500,error_messages={
               'required': 'This is a short view about your story so you have to provide something meaningful'
                }, widget=forms.TextInput(
     attrs={
         "class": """leading-none text-gray-50 p-3 focus:outline-none
                  focus:border-blue-700 mt-4 border-0 bg-gray-800 rounded"""
     }
    ))

    class Meta:
        model = Post
        exclude = ('date', 'slug', 'author')
