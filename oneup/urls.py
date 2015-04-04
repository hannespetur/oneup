from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'oneup.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url (r'^$', 'oneup.views.index.page', name="public_index"),
	url (r'^index$', 'oneup.views.index.page'),
	url (r'^about$', 'oneup.views.about.page', name="public_about"),
    url (r'^admin/', include(admin.site.urls)),
]
