from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^register', 'register'),
    url(r'^login', 'login'),
    url(r'^logout', 'logout'),
)