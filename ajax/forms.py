from django import forms
from django.forms import widgets

from .models import Post, PostImage


class PostModelForm(forms.ModelForm):
    
    images = forms.ImageField(widget=widgets.ClearableFileInput(
        attrs={
            'multiple': 'true',
            'id':       'multiple-image-post',
            'class':    'custom-hidden'
        }),
        required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control'
            })

    def clean(self):
        data = super().clean()
        if data['title']:
            title = data['title']
            if len(title) < 5:
                self.add_error(
                    'title', 'Заголовок должен быть больше 5 символов')
            if Post.objects.filter(title=title).exists():
                self.add_error('title', 'Такой заголовок уже существует')
        if data['text']:
            text = data['text']
            if len(text) < 10:
                self.add_error('text', 'Длина должна быть больше 10 символов')
        return data

    def save(self, commit=True):
        super().save(commit=commit)
        images = self.files.getlist('images')
        for image in images:
            PostImage.objects.create(post=self.instance, image=image)

    class Meta:
        model = Post
        exclude = ('created_at', )
