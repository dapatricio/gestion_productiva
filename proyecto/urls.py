from django.conf.urls import url, patterns
from proyecto import views

urlpatterns = patterns('proyecto.views',
    url(r'^index$', 'index', name='index'),
    url(r'^mapa$', 'mapa', name='mapa'),
    url(r'^contacto$', 'contacto', name='contacto'),
    url(r'^discapacidadesPastel$', 'discapacidadesPastel', name='discapacidadesPastel'),
    url(r'^analfabetismo$', 'analfabetismo', name='analfabetismo'),
    url(r'^mental$', 'mental', name='mental'),
    url(r'^visual$', 'visual' , name='visual'),
    url(r'^auditiva$', 'auditiva', name='auditiva'),
    url(r'^fisica$', 'fisica', name='fisica'),
    url(r'^intelectual$', 'intelectual', name='intelectual'),
)

