from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('accounts.urls', namespace='accounts')),
    url(r'^products/api/', include('products.api.urls', namespace='products-api')),
    url(r'^products/', include('products.urls', namespace='products')),
    # url(r'^accounts/', include('accounts.urls')),

]

