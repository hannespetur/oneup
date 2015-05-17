from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'oneup.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url (r'^$', 'oneup.apps.test.views.index.page', name="public_index"),
	url (r'^index$', 'oneup.apps.test.views.index.page'),
	url (r'^about$', 'oneup.apps.test.views.about.page', name="public_about"),
    url (r'^admin/', include(admin.site.urls)),
    url (r'^polls/', include('oneup.apps.test.views.polls.urls', namespace="polls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
