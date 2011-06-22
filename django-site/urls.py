from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^tictactoe/', include('apps.tictactoe.urls')),
    url(r'^$', 'apps.staticpages.views.index'),
    # Examples:
    # url(r'^$', 'tictactoe.views.home', name='home'),
    # url(r'^tictactoe/', include('tictactoe.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
