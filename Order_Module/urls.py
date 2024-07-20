from django.urls import path

from Order_Module.views import *

urlpatterns = [
    path('', CartView.as_view(), name='cart_url'),
    path('add-product/<str:product_name>/<int:product_id>/', AddProductView.as_view(), name='add_product_url'),
    path('increase-count/', IncreaseCount.as_view(), name='increase_count_url'),
    path('decrease-count/', DecreaseCount.as_view(), name='decrease_count_url'),
    path('remove-product/<str:product_name>/<int:product_id>', RemoveProduct.as_view(), name='remove_product_url'),
    path('submit-order/', SubmitOrder.as_view(), name='submit_order_url'),
]