# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Analfabestismo(models.Model):
    id_analfabetismo = models.IntegerField(primary_key=True)
    id_parroquia = models.ForeignKey('Parroquia', db_column='id_parroquia')
    analfabeto = models.IntegerField()
    area = models.CharField(max_length=-1)
    alfabeto = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'analfabestismo'

class Canton(models.Model):
    id_canton = models.IntegerField(primary_key=True)
    id_provincia = models.ForeignKey('Provincia', db_column='id_provincia')
    nombre_canton = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'canton'


class Cantpob(models.Model):
    id_cantpob = models.IntegerField(primary_key=True)
    id_canton = models.ForeignKey(Canton, db_column='id_canton')
    id_poblacion5anios = models.ForeignKey('Poblacion5Anios', db_column='id_poblacion5anios')
    id_filtro = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cantpob'


class Discapacidad(models.Model):
    id_discapacidad = models.IntegerField(primary_key=True)
    no = models.IntegerField()
    si = models.IntegerField()
    area = models.CharField(max_length=-1)
    menor12 = models.CharField(max_length=-1)
    id_tipo = models.ForeignKey('Tipo', db_column='id_tipo')

    class Meta:
        managed = False
        db_table = 'discapacidad'


class Parrodis(models.Model):
    id_parrodis = models.IntegerField(primary_key=True)
    id_discapacidad = models.ForeignKey(Discapacidad, db_column='id_discapacidad')
    id_parroquia = models.ForeignKey('Parroquia', db_column='id_parroquia')

    class Meta:
        managed = False
        db_table = 'parrodis'


class Parroquia(models.Model):
    id_parroquia = models.IntegerField(primary_key=True)
    id_canton = models.ForeignKey(Canton, db_column='id_canton')
    nombre_parroquia = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'parroquia'


class Poblacion5Anios(models.Model):
    id_poblacion5anios = models.IntegerField(primary_key=True)
    centro = models.IntegerField()
    ninguno = models.IntegerField()
    primario = models.IntegerField()
    secundario = models.IntegerField()
    basica = models.IntegerField()
    preescolar = models.IntegerField()
    bachillerato = models.IntegerField()
    id_tipo = models.ForeignKey('Tipo', db_column='id_tipo')
    superior = models.IntegerField()
    postbachillerato = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'poblacion5anios'


class Provincia(models.Model):
    id_provincia = models.IntegerField(primary_key=True)
    nombre_proncia = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'provincia'


class Tipo(models.Model):
    id_tipo = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'tipo'
