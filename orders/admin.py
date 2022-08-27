from django.contrib import admin

from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'quantity', 'size',
                    'order_status', 'updated_at')
    list_filter = ('order_status', 'updated_at')
    # fields = [('email', 'password'), ('username', 'phone_number'),
    #           ('first_name', 'last_name')]


admin.site.register(Order, OrderAdmin)
