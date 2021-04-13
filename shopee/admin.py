from django.contrib import admin
from .models import Buyer


class BuyerAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_id', 'phone_number', 'start_date', 'end_date')


admin.site.register(Buyer, BuyerAdmin)
