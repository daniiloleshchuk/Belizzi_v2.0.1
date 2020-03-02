from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from products import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

from django.conf import settings

urlpatterns = [
    url(r'^product/(?P<product_id>\w+)/$', views.product, name='product'),
    url(r'^product/', views.product, name='product')


]

if settings.DEBUG:
    if settings.MEDIA_ROOT:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()


