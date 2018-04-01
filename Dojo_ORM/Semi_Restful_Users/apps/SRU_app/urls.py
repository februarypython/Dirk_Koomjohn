from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^users$", views.index, name="index"),
    url(r"^users/new$", views.new, name="new"),
    url(r"^users/create$", views.create, name="create"),
    url(r'^users/(?P<id>\d+)$', views.show, name="show"),
    url(r'^users/(?P<id>\d+)/edit$', views.edit, name="edit"),
    url(r"^users/(?P<id>\d+)/update$", views.update, name="update"),
    url(r'^users/(?P<id>\d+)/destroy$', views.destroy, name="destroy"),
]

