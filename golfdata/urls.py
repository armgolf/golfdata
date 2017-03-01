from django.conf.urls import include, url
from django.contrib import admin
from golfapp import views
from django.contrib.auth import views as auth_views
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

urlpatterns = [
    url('^accounts/register/', CreateView.as_view(
            template_name='registration/register.html',
            form_class=UserCreationForm,
            success_url='/'
    ), name='register'),
    url('^accounts/', include('django.contrib.auth.urls')),
    url(r'^$', views.homepage, name='homepage'),
    url(r'^dashboard/$', views.display, name='display'),
    url(r'^golfscore/$', views.golfscore_entry, name='golfscore_entry'),
    url(r'^golfscore/(?P<pk>\d+)/$', views.golfscore_detail, name='golfscore_detail'),
    url(r'^golfscore/(?P<pk>\d+)/edit/$', views.golfscore_edit, name='golfscore_edit'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', auth_views.login, name='login'),
    url(r'^accounts/logout/$', auth_views.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'^charts/$', views.plot, name='plot'),
    url(r'^charts2/$', views.plot2, name='plot2'),
    url(r'^charts3/$', views.plot3, name='plot3'),
    url(r'^drivingtips/$', views.drivingtips, name='drivingtips'),
    url(r'^longirontips/$', views.longirontips, name='longirontips'),
    url(r'^approachtips/$', views.approachtips, name='approachtips'),
    url(r'^chippingtips/$', views.chippingtips, name='chippingtips'),
    url(r'^puttingtips/$', views.puttingtips, name='puttingtips'),
]
