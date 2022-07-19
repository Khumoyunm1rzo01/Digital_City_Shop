from re import M
from django.contrib import admin
from django.urls import path, include
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )
from .views import *


urlpatterns = [
    path('user/register/', User_Register),
    path('get-slider/', Get_Slider),
    path('product/filter/sale/', On_Sale),
    path('product/filter/price/', Product_price),
    path('join/news/', Join_Newsletter),
    path('product_id/<int:pk>', product_id),
    path('get-product/', Getproduct),
    path('get-info/', Info_View.as_view()),
    path('get-blog/', Getblog),
    path('post-contact/', Postcontact),
    path('post-comment/', Postcomment),
    path('post-reply/', Postreply),
    path('get-cookies/', Getcookies),
    path('get-privacypolicy/', Getprivacy),
    path('get-about/', Getabout),
    path('get-requirements/', Getrequirements),
    path('get-toptrends/', Gettoptrends),
    path('get-deliveryoptions/', Getdelivery),
    path('get-order/', Getorder),
    path('get-orderitem/', Getorderitem),
    path('get-shippingdetail/', Getshippingsdetail),
    path('get-cart/', Cart_View.as_view()),
    path('get-cartdetail/', Getcartdetail),
    path('get-billingdetails/', Getbillingdetail),
    path('rating/new/<int:pk>/', Create_Rating),
    path('post-card/', Add_Cart),
    path('post-wishlist/', Add_Wishlist),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

