from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100, verbose_name='razón social')
    rut = models.CharField(max_length=100, null=True, blank=True, verbose_name='rut / run')

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.name