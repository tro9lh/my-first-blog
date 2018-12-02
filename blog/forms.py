from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('name', 'surname','patronymic','DateofBirth',
        'sex','img')

class PostForm2(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('hairСolor','weight')

class PostForm3(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('favoriteAnimal','haveAnimal',)
