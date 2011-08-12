from django.conf.urls.defaults import *
from django.views.generic import ListView,DetailView
from django.contrib.auth.views import login,logout
from wikilink.views import new_source,new_source_from_url,SourceListView,irrelevant,mycitations
from wikilink.models import Source

urlpatterns = patterns('wikilink.views',
    #(r'^$', 'index'),
    url(r'^$',SourceListView.as_view(),name="source_list"),
    url(r'^(?P<pk>\d+)/$', DetailView.as_view(model=Source),name="source_detail"),
    url(r'^newsource/$',new_source,name="new_source"),
    url(r'^newurl/$',new_source_from_url,name="new_url"),
    url(r'^irrelevant/$',irrelevant,name="remove_irrelevant"),
    url(r'^login/$',login,name="login"),
    url(r'^logout/$',logout,{'next_page':'/link'},name="logout"),
    url(r'^mycitations/$',mycitations,name="mycitations")
   #Future  url(r'^users/(?P<username>[A-Za-z0-9_\@\+\.\_]+)/$',usercitations,name="user_citations")
)