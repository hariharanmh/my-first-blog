from django.conf.urls import url
from .views import ( 
	CustomerListView,
	CustomerDetailView,
	CustomerCreateView,
	CustomerUpdateView,
	CustomerDeleteView,
	CustomerTodayArchiveView,
	CustomerYearArchiveView,
	)  

urlpatterns = [
	url(r'^create/$', CustomerCreateView.as_view(), name='create'),
	url(r'^today/$', CustomerTodayArchiveView.as_view(), name='archive_today'),
	url(r'^(?P<year>[0-9]{4})/$', CustomerYearArchiveView.as_view(), name="article_year_archive"),
    url(r'^(?P<slug>[\w-]+)/$', CustomerDetailView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/update/$', CustomerUpdateView.as_view(), name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', CustomerDeleteView.as_view(), name='delete'),
    url(r'$', CustomerListView.as_view(), name='list'),
]