from django.urls import path
from accounts.views import login_page, register_page , activate_email, add_to_cart, cart, remove_cart, remove_coupon, success, userprofile, logout, update_address, wishlist
#from products.views import add_to_cart
#from accounts.views import cart

urlpatterns = [
    path('login/', login_page, name="login"),
    path('register/', register_page, name="register"),
    path('activate/<email_token>/', activate_email, name = "activate_email"),
    path('cart/', cart, name = "cart"),
    path('add-to-cart/<uid>/', add_to_cart, name = "add_to_cart"),
    path('remove-cart/<cart_item_uid>/', remove_cart, name="remove_cart"),
    path('remove_coupon/<cart_id>/', remove_coupon, name="remove_coupon"),
    path('success/', success, name="success"),
    path('userprofile/', userprofile, name = "userprofile"),
    path('wishlist/', wishlist, name = "wishlist"),
    path('logout/', logout, name="logout"),
    path('update_address/', update_address, name="update_address")
    #path('/userprofile', userprofile, name="userprofile")
    #path('products/', products, name="products")
]