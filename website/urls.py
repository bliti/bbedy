from django.conf.urls import patterns, url

urlpatterns = patterns('website.views',
    url(r'^$', 'index'),
    url(r'^reset/', 'reset'),
    url(r'^user/reset/', 'reset_user'),
    url(r'^signup/', 'signup'),
    url(r'^error/signup/', 'signup_error'),
    url(r'^welcome/', 'welcome'),
    url(r'^error/user/', 'user_error'),
    url(r'^user/', 'user_updated'),
    
    
)