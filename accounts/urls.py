from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from . import views

app_name = 'accounts'
urlpatterns = [

                  url(r'^$', views.index_display, name='index_display'),
                  url(r'^login/$', views.user_login, name='login_user'),
                  # url(r'^register/$', views.UserFormView.as_view(), name='register'),
                  url(r'logout/$', views.logout_user, name='logout'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
"""
the above setting is for serving the static files during development. The setting will be changed when the system
is set for deployment. remember to import SETTINGS and STATIC
"""
