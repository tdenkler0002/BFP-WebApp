
from django.conf.urls import include, url
from django.contrib import admin
from main import views

from main.forms import AuthenticationForm
from django.contrib.auth.views import login, logout


urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^', include('main.urls')),
    url(r'^admin/', include(admin.site.urls)),
]


urlpatterns += [
    url(r'^accounts/login/$', login, {
        'template_name': 'login.html', 
        'authentication_form': AuthenticationForm
    }, name='login'),
    url(r'^accounts/logout/$', logout, {
        'next_page': '/'
    }, name='logout'),
]

