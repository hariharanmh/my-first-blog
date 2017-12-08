from django.conf.urls import url
from .views import (
	ShopListView,
	ShopDetailView,
	ShopCreateView,
	ShopUpdateView,
	)  

urlpatterns = [
	url(r'^create/$', ShopCreateView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/$', ShopDetailView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/update/$', ShopUpdateView.as_view(), name='update'),
    url(r'^$', ShopListView.as_view(), name='list'),
]