from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
#fds

from django.contrib.auth.views import login, logout




urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fein_cms.views.home', name='home'),
    # url(r'^fein_cms/', include('fein_cms.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static'}),
    url(r'^comments/', include('django.contrib.comments.urls')),
    #url('^irc/', include('gnotty.urls')),
)


urlpatterns += patterns('highlight.views',
    url(r'^code/', 'createCode'),
    url(r'^codes/(?P<user_name>\w+)/(?P<code_name>\S+)/', 'show'),
    #url(r'^codes/(?P<code_name>\w+)/$', 'show'),

)

urlpatterns += patterns('auth.views',
    #url(r'^accounts/', include('auth.urls')),
    url(r'^accounts/register', 'register'),
    url(r'^accounts/login', 'login'),
    url(r'^accounts/logout', 'logout'),
    #url(r'^accounts/edit', 'edit'),

)

urlpatterns += patterns('cms.views',
    (r'^home/$', 'home'),
    (r'^$', 'home'),
    url(r'^help/$', 'help'),
    url(r'^about/$', 'about'),
    url(r'', include('social_auth.urls')),
)

urlpatterns += staticfiles_urlpatterns()





