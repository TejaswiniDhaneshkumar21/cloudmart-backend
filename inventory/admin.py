from django.contrib import admin
from .models import Product, Order, OrderItem


# --- Product admin configuration ---
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # columns to show in the product list
    list_display = ("name", "sku", "price", "quantity_in_stock", "is_active")
    # allow searching by these fields
    search_fields = ("name", "sku")
    # filters on the right side
    list_filter = ("is_active",)


# --- Order admin configuration ---
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "customer_name", "status", "created_at")
    search_fields = ("customer_name",)
    list_filter = ("status", "created_at")


# --- OrderItem admin configuration ---
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "product", "quantity", "unit_price")
    list_filter = ("product",)


# --- Change the admin branding (titles) ---
admin.site.site_header = "CloudMart Admin"              # big text at the top
admin.site.site_title = "CloudMart Admin Portal"        # text in browser tab
admin.site.index_title = "Welcome to CloudMart Dashboard"  # text on main admin page
