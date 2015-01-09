from django.conf.urls import patterns
from django.conf.urls import url
from rest_framework_swagger.views import SwaggerResourcesView, SwaggerApiView, SwaggerUIView


urlpatterns = patterns(
    '',
    url(r'^$', SwaggerUIView.as_view(), name="django.swagger.base.view"),
    url(r'^api-docs/$', SwaggerResourcesView.as_view(), name="django.swagger.resources.view"),
    url(r'^api-docs/(?P<path>.*)/?$', SwaggerApiView.as_view(), name='django.swagger.api.view'),
    url(r'^v(?P<api_version>[0-9.]+)/$', SwaggerUIView.as_view(), name="django.swagger.base.view"),
    url(r'^v(?P<api_version>[0-9.]+)/api-docs/$', SwaggerResourcesView.as_view(), name="django.swagger.resources.view"),
    url(r'^v(?P<api_version>[0-9.]+)/api-docs/(?P<path>.*)/?$', SwaggerApiView.as_view(), name='django.swagger.api.view'),
)
