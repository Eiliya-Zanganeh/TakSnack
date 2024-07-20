from django.contrib import admin
from Order_Module.models import OrderModel


@admin.register(OrderModel)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone_number', 'is_ordered']
    search_fields = ['full_name', 'phone_number']
    list_filter = ['is_ordered', 'phone_number', 'full_name']
    list_editable = ['is_ordered']
