from django.db import models

class Mineral(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название полезного ископаемого")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    extraction_url = models.URLField(verbose_name="Ссылка на добычу (Datawrapper)")
    reserves_url = models.URLField(verbose_name="Ссылка на запасы (Datawrapper)")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Полезное ископаемое"
        verbose_name_plural = "Полезные ископаемые"