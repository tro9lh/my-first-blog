from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('name', 'surname','patronymic','DateofBirth',
        'sex',)

class PostForm2(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('img','hairСolor','weight',)

class PostForm3(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('favoriteAnimal','haveAnimal',)
