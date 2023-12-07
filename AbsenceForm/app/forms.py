from django import forms
from .models import Post, File
from bootstrap_datepicker_plus.widgets import DatePickerInput


class PostCreateForm(forms.ModelForm):
    date = forms.DateField(
        label='欠席する日',
        widget=DatePickerInput(format='%Y-%m-%d')
    )

    class Meta:
        model = Post
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


FileFormset = forms.inlineformset_factory(
    Post, File, fields='__all__',
    extra=1, can_delete=False
)
