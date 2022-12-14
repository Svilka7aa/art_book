from django import forms

from art_book.common.models import PhotoLike, PhotoComment
from art_book.core.form_mixins import DisabledFormMixin
from art_book.photos.models import Photo


class PhotoBaseForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ('publication_date', "user")


class PhotoCreateForm(PhotoBaseForm):
    pass


class PhotoEditForm(PhotoBaseForm):
    class Meta:
        model = Photo
        exclude = ('publication_date', 'photo')


class PhotoDeleteForm(DisabledFormMixin, PhotoBaseForm):
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        if commit:
            self.instance.tagged_pets.clear()  # many-to-many

            Photo.objects.all() \
                .first().tagged_pets.clear()
            PhotoLike.objects.filter(photo_id=self.instance.id) \
                .delete()
            PhotoComment.objects.filter(photo_id=self.instance.id) \
                .delete()
            self.instance.delete()

        return self.instance