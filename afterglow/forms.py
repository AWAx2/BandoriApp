from django import forms


class PhotoForm(forms.Form):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class':'custom-file-input'}))


class ContactForm(forms.Form):
    name = forms.CharField(label='お名前', max_length=30)
    email = forms.EmailField(label='メールアドレス')
    title = forms.CharField(label='タイトル', max_length=30)
    message = forms.CharField(label='メッセージ', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # bootstrapのフォーム用クラスの追加
        self.fields['name'].widget.attrs['class'] = 'form-control col-12'
        self.fields['name'].widget.attrs['placeholder'] = 'お名前'

        self.fields['email'].widget.attrs['class'] = 'form-control col-12'
        self.fields['email'].widget.attrs['placeholder'] = 'メールアドレス'

        self.fields['title'].widget.attrs['class'] = 'form-control col-12'
        self.fields['title'].widget.attrs['placeholder'] = 'タイトル'

        self.fields['message'].widget.attrs['class'] = 'form-control col-12'
        self.fields['message'].widget.attrs['placeholder'] = 'メッセージ'
