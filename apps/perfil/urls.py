from django.conf.urls import url, include

from views import login_views, register_views

urlpatterns = [
    url(r'^$', login_views, name='login'),
    url(r'^registro/$', register_views, name='registro'),
 ]
