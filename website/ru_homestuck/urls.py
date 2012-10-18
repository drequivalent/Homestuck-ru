from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^$', 'ru_homestuck.views.display_page'),
    url(r'^page/$', 'ru_homestuck.views.display_page'),
    url(r'^page/(?P<page_number>\d+)/$', 'ru_homestuck.views.display_page'),

)
