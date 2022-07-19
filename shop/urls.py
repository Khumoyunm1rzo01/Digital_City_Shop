from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('index/', Index, name="index"),
    path('default/', Default, name="default"),
    path('general-widget/', General, name="general-widget"),
    path('chart-widget/', Chart, name="chart-widget"),
    path('boxed-layout/', Boxed_Layout, name="box-layout"),
    path('social-app/', Social_App, name="social-app"),
    path('blogs/all/', Blogs_Get, name='blogs-get'),
    path('avatars/', Avatars, name="avatars"),
    path('product/', Mahsulot, name="product"),
    path('product-page/', Product_Page, name="product-page"),
    path('product-list/', Product_List, name="product-list"),
    path('payment-details/', Payment_Details, name="payment-details"),
    path('order-history/', Order_History, name="order-history"),
    path('cart/', Cart_function, name="cart"),
    path('wish-list/', Wish_List, name="wish-list"),
    path('checkout-product/', Checkout, name="checkout"),
    path('pricing/', Pricing, name="pricing"),
    path('chat/', Chat, name="chat"),
    path('user-profile/', User_Profile, name="user-profile"),
    path('edit-profile/', Edit_profile, name="edit-profile"),
    path('users-cards/', Users_Cards, name="users-cards"),
    path('bookmark/', Bookmark, name="bookmark"),
    path('tasks/', Tasks, name="tasks"),
    path('todo/', To_Do, name="to-do"),
    path('contact/', Contact_02, name="contact_02"),
    path('blog/',Blog_01, name="blog-01"),
    path('blog-single/', Blog_Single, name="blog-single"),
    path('add-post/', Add_post, name="add-post"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
