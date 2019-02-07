from django.conf.urls import url
from . import views


urlpatterns = [
    url(
        r'^api/v1/groceries/(?P<pk>[0-9]+)$',
        views.get_delete_update_grocery,
        name='get_delete_update_grocery'
    ),
    url(
        r'^api/v1/groceries/$',
        views.get_post_groceries,
        name='get_post_groceries'
    )
]
