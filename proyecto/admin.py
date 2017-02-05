from django.contrib import admin

# Register your models here.

from proyecto.models import Provincia, Canton, Parroquia, Analfabestismo, Cantpob, Discapacidad, Parrodis, Poblacion5Anios, Tipo

admin.site.register(Provincia)
admin.site.register(Canton)
admin.site.register(Parroquia)
admin.site.register(Analfabestismo)
admin.site.register(Cantpob)
admin.site.register(Discapacidad)
admin.site.register(Parrodis)
admin.site.register(Poblacion5Anios)
admin.site.register(Tipo)