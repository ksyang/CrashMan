from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
	url(r'^form/',views.form_view,name='form_view'),
	url(r'^crash/(?P<ip>.+)/(?P<program>.+)/',views.crash_view ,name='crash_view'),
	url(r'^delete/(?P<Vm_name>.+)/',views.vm_delete,name='vm_delete'),
	url(r'^ddelete/(?P<Docker_name>.+)/',views.docker_delete,name='docker_delete'),
]
