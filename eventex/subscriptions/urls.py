from django.urls import path, re_path

from eventex.subscriptions.views import new, detail

app_name = 'subscriptions'

urlpatterns = [
    path('', new, name='new'),
    re_path(r'^(?P<pk>\d+)/$', detail, name='detail'),
]
