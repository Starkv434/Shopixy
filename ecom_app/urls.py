from django.urls import path
from . import views


urlpatterns = [
    path("home", views.home, name = "home"),
    path("category/<str:category_name>", views.category, name = "category"),
    path("specific_product/<str:product_name>", views.specific_product, name = "specific_product"),
    path("product/<str:uid>", views.product, name = "product"),
    path("contact/", views.contact, name = "contact"),
    path("about/", views.about, name = "about"),
    path("search/", views.search, name = "search"),
    
    

    path('add-to-cart/<str:uid>',views.add_to_cart, name="add_to_cart"),
    path('show_cart/', views.show_cart, name="show_cart"),
    path('pluscart/', views.pluscart, name="pluscart"),
    path('minuscart/', views.minuscart, name="minuscart"),
    path('removecart/', views.removecart, name="removecart"),
    path('plus_wishlist/', views.plus_wishlist, name="plus_wishlist"),
    path('minus_wishlist/', views.minus_wishlist, name="minus_wishlist"),
    path('show_wishlist/', views.show_wishlist, name="show_wishlist"),
    
    path("orders/", views.orders, name = "orders"),
    path('checkout/', views.checkout, name="checkout"),
    path("payment_success/", views.payment_success, name="payment_success"),
    path("payment_failed/", views.payment_failed, name="payment_failed"),
]