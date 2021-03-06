from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('apps.tictactoe',
    url(r'newgame/?$', 'views.newGame'),
    url(r'makemove/x/(?P<x>\d+)/y/(?P<y>\d+)/?$', 'views.makeMove'),
    url(r'getmove/?$', 'views.getMove'),
)
