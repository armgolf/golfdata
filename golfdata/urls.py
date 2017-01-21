from django.conf.urls import include, url
from django.contrib import admin
from golfapp import views
urlpatterns = [
    url(r'^$', views.display, name='display'),
    url(r'^golfscore/$', views.golfscore_entry, name='golfscore_entry'),
    url(r'^golfscore/(?P<pk>\d+)/$', views.golfscore_detail, name='golfscore_detail'),
    url(r'^golfscore/(?P<pk>\d+)/edit/$', views.golfscore_edit, name='golfscore_edit'),
    url(r'^admin/', include(admin.site.urls)),
]
