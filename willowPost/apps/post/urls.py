from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
import views


urlpatterns=patterns('',
        url(r'^authors', views.AuthorList.as_view()),
        url(r'^posts', views.PostList.as_view()),
        url(r'^authors/$', views.AuthorList.as_view()),
        url(r'^posts/$', views.PostList.as_view()),
        url(r'^posts/(?P<pk>\d+)/$', views.PostDetails.as_view(),name="post_details"),
        url(r'^authors/(?P<pk>\d+)/$', views.AuthorDetails.as_view(),name="author_details"),
)
urlpatterns = format_suffix_patterns(urlpatterns)
