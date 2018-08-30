from django.conf.urls import url,include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from customer.views import ContactView,VideoView,IndexView,AboutView,RegisterCustomer,WedView,DecorView,PhotoView
from django.contrib.auth import views as auth_views
from customer import views

urlpatterns = [
   url(r'^about/',AboutView.as_view(),name='abt'),
   url(r'^login/$', views.login, name='login'),
   url(r'^wed/',WedView.as_view(),name='wed'),
   url(r'^dec/',DecorView.as_view(),name='decor'),
   url(r'^photography/',PhotoView.as_view(),name='photo'),
   url(r'^custregister/$', RegisterCustomer.as_view(), name='register'),
   url(r'^contact/$',ContactView.as_view(),name='contact'),
   url(r'^home/$',IndexView.as_view(),name='index'),
   url(r'^video/$',VideoView.as_view(),name='video'),
  


]

urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
