from django.conf.urls import url,include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from eventapp.views import EventView,AdminView,ListEvent,EditEvent,BookEvent,Order

urlpatterns = [
	 url(r'^addevent/$',EventView.as_view(),name='add_event'),
	 url(r'^list/$',ListEvent.as_view(),name='list_event'),
	 url(r'^editevent/(?P<pk>[0-9]+)/$',EditEvent.as_view(),name='edit_event'),
	 url(r'^book/$',BookEvent.as_view(),name='book_event'),
	 url(r'^adminhome/$',AdminView.as_view(),name='adminhome'),
	 url(r'order/(?P<pk>[0-9]+)/$',Order.as_view(),name='orders'),
	 ]


urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
