from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'oscars/actors/$', 'oscars.actors.views.index'),
    (r'oscars/actors/(?P<id>\d+)/$', 'oscars.actors.views.detail'),
    (r'oscars/admin/', include(admin.site.urls)),
    (r'oscars/actors/decade_10.html', 'oscars.actors.views.children'),
    (r'oscars/actors/decade_20.html', 'oscars.actors.views.twenties'),
    (r'oscars/actors/decade_30.html', 'oscars.actors.views.thirties'),
    (r'oscars/actors/decade_40.html', 'oscars.actors.views.fourties'),
    (r'oscars/actors/decade_50.html', 'oscars.actors.views.fifties'),
    (r'oscars/actors/decade_60.html', 'oscars.actors.views.sixties'),
    (r'oscars/actors/decade_70.html', 'oscars.actors.views.seventies'),
    (r'oscars/actors/browse_age.html', 'oscars.actors.views.browse_age'),
    (r'oscars/actors/browse_name.html', 'oscars.actors.views.browse_name')
)
