import uuid

from django.db import models


class UUIDAbstractModel(models.Model):
    id = models.UUIDField(
        verbose_name='ID',
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    class Meta:
        abstract = True


class Region(UUIDAbstractModel):
    name = models.CharField('название', max_length=100)
    parent = models.ForeignKey(
        to='self',
        on_delete=models.CASCADE,
        verbose_name='входит в',
        related_name='subregions',
        null=True,
        blank=True,
    )
    order = models.PositiveSmallIntegerField('порядок')

    class Meta:
        verbose_name = 'регион'
        verbose_name_plural = 'регионы'
        ordering = ('order', 'name')

    def __str__(self):
        return self.name


class Country(UUIDAbstractModel):
    short_name = models.CharField('краткое наименование', max_length=100)
    full_name = models.CharField('полное наименование', max_length=100, blank=True)
    numeric_code = models.CharField('цифровой код', max_length=10)
    alpha2_code = models.CharField('альфа-2', max_length=10)
    alpha3_code = models.CharField('альфа-3', max_length=10)
    region = models.ForeignKey(
        to=Region,
        on_delete=models.SET_NULL,
        verbose_name='регион',
        related_name='countries',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'страна'
        verbose_name_plural = 'страны'
        ordering = (
            'numeric_code',
            'short_name',
            'alpha2_code',
            'alpha3_code',
        )

    def __str__(self):
        return self.short_name
