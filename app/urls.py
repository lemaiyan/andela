from django.conf.urls import url
from app.views import *

urlpatterns = [
    url('^get_image/(?P<dimensions>\w+)/(?P<text>\w+)/$', get_image_view, name='get_image'),
]
