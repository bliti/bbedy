from django.conf.urls import patterns, url

urlpatterns = patterns('api.views',
    url(r'^messages/', 'messages'),
    url(r'^send/', 'send'),
)