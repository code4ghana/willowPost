from django.conf.urls import patterns, include, url
from apps.post.models import Author,Post

urlpatterns = patterns('',
    (r'^', include('willowPost.apps.post.urls')),
    #(r'^api-doc', include('rest_framework_swagger.urls', namespace='swagger')),
)
