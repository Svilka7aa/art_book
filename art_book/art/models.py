from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

UserModel = get_user_model()


class Art(models.Model):
    MAX_NAME_LEN = 30
    MAX_TYPE_LEN = 30

    # TODO add more types of art

    PAINTING = "painting"
    SCULPTURE = "sculpture"
    GRAFfITI = "graffiti"

    art = (
        (PAINTING, PAINTING),
        (SCULPTURE, SCULPTURE),
        (GRAFfITI, GRAFfITI),
    )

    name = models.CharField(
        max_length=MAX_NAME_LEN,
        null=False,
        blank=False,
    )

    type = models.CharField(
        max_length=MAX_TYPE_LEN,
        choices=art,
        null=False,
        blank=False,
    )

    photo = models.URLField(
        null=False,
        blank=False,
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
    )

    creation_date = models.DateField(
        null=True,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    price = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f'{self.id}-{self.name}')

        return super().save(*args, **kwargs)

