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
