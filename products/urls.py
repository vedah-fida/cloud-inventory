from django.conf.urls import include, url

from . import views
app_name = "products"

urlpatterns = [
    url(r'', views.products_base, name="products"),
    url(r'^view/', views.products_inner_view, name="product_details"),

]
