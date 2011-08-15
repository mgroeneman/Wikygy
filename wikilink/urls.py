from django.conf.urls.defaults import *
from django.views.generic import ListView,DetailView
from django.contrib.auth.views import login,logout
from wikilink.views import new_source,new_source_from_url,SourceListView,source_detail,workbench,update_rss
from wikilink.models import Source

urlpatterns = patterns('wikilink.views',
    # (r'^$', 'index'),
    url(r'^$',SourceListView.as_view(),name="source_list"),
    url(r'^(uncited)/$',SourceListView.as_view(),name="uncited"),
    url(r'^(?P<pk>\d+)/$', source_detail,name="source_detail"),
    url(r'^(?P<pk>\d+)/(?P<action>cite|irrelevant|watch)/$',source_detail,name="source_detail_action"),
    url(r'^newsource/$',new_source,name="new_source"),
    url(r'^newurl/$',new_source_from_url,name="new_url"),
    url(r'^rss/(?P<rssid>\d+)/$',SourceListView.as_view(),name="rss_detail"),
    url(r'^rss/update$',update_rss,name="update_rss"),
    url(r'^login/$',login,name="login"),
    url(r'^logout/$',logout,{'next_page':'/link'},name="logout"),
    url(r'^workbench/$',workbench,name="workbench"),
   #Future  url(r'^users/(?P<username>[A-Za-z0-9_\@\+\.\_]+)/$',usercitations,name="user_citations")
)