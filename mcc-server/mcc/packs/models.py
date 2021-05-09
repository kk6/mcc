from django.db import models
from django.core.validators import FileExtensionValidator


class CitPack(models.Model):
    name = models.CharField(max_length=255, verbose_name="名前", unique=True)
    official_site = models.URLField(verbose_name="公式サイト", null=True, blank=True)
    catalog_url = models.URLField(verbose_name="カタログURL", null=True, blank=True)
    icon = models.ImageField(
        verbose_name="アイコン",
        upload_to="cit_packs",
        validators=[FileExtensionValidator(["jpg", "png"])],
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name_plural = "CITパック"
        db_table = "cit_packs"
