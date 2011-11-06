from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'inventory.views.index'),
    (r'^all$', 'inventory.views.all'),
    (r'^login$', 'inventory.views.user_login'),
    (r'^logout$', 'inventory.views.user_logout'),
    (r'^object/(\d+)$', 'inventory.views.object_view'),
    (r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':
    settings.MEDIA_ROOT}),
)
