from django.conf.urls import url, include
from django.contrib import admin
import Auction_system.views
from classviews import *
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', Auction_system.views.index, name="index"),
    url(r'^viewproduct/', login_required(View.as_view()), name="product_view"),
    url(r'^addproduct/', login_required(CreateProductView.as_view()), name="product_add"),
    url(r'^productdetails/(?P<pk>[0-9]+)', login_required(ProductDetailView.as_view()), name="product_detail"),
    url(r'^register_user/', UserCreateView.as_view(), name="register"),

    url(r'^deleteproduct/(?P<pk>[0-9]+)', login_required(ProductDelete.as_view()), name="delete_product"),
    url(r'^bidderlist/(?P<pk>[0-9]+)', login_required(BuyerListView.as_view()), name="bidder_list"),
    url(r'^logout/', 'django.contrib.auth.views.logout_then_login')
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
