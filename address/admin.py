from django.contrib import admin
from django.utils.safestring import mark_safe
from address.models import Address


class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'street_address', 'apartment_address', 'zip_code')
    list_display_links = ("user",)
    # search_fields = ("name", "id")
    # list_filter = ("name", "status", "featured")
    fields = (('user',), 'street_address', 'apartment_address', ('country', 'state', 'city'), ('zip_code', 'address_type', 'default'), ('longetude', 'latitude'))

    # fieldsets = [
    #     (None, {'fields': ['id', 'name', 'image']}),
    #     ('Advance information', {'fields': ['status', 'featured', 'created_at', 'updated_at'], 'classes':['collapse']}),
    # ]


admin.site.register(Address, AddressAdmin)
