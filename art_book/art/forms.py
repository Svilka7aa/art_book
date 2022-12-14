from django import forms

from art_book.art.models import Art
from art_book.core.form_mixins import DisabledFormMixin


class ArtBaseForm(forms.ModelForm):
    class Meta:
        model = Art
        fields = '__all__'
        exclude = ('slug',)
        labels = {
            'name': 'Art Name',
            'photo': 'Link to Image',
            'creation_date': 'Date Creation',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Art name'
                }
            ),
            'creation_date': forms.DateInput(
                attrs={
                    'placeholder': 'mm/dd/yyyy',
                    'type': 'date',
                }
            ),
            'photo': forms.URLInput(
                attrs={
                    'placeholder': 'Link to image',
                }
            )
        }


class ArtCreateForm(ArtBaseForm):
    pass


class ArtEditForm(DisabledFormMixin, ArtBaseForm):
    disabled_fields = ('name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()


class ArtDeleteForm(DisabledFormMixin, ArtBaseForm):
    disabled_fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
