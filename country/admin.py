from django.contrib import admin
from country.models import Country, State, City
# Register your models here.
admin.site.index_title = 'Country'
admin.empty_value_display = '**Empty**'


class StateInline(admin.TabularInline):
    model = State
    extra = 1

    classes = ("grp-collapse grp-open",)
    fieldsets = (
        ("", {
            "fields": ("name", "country"),
        }),
    )


class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')
    list_display_links = ("name",)
    search_fields = ("name",)
    list_filter = ("status",)
    inlines = [StateInline]


admin.site.register(Country, CountryAdmin)


class CityInline(admin.TabularInline):
    model = City
    extra = 1

    classes = ("grp-collapse grp-open",)
    fieldsets = (
        ("", {
            "fields": ("name", "state"),
        }),
    )


class StateAdmin(admin.ModelAdmin):
    list_display = ('country', 'name', 'status')
    list_display_links = ("name",)
    search_fields = ("name", 'country')
    list_filter = ("status", 'country')
    inlines = [CityInline]


admin.site.register(State, StateAdmin)


class CityAdmin(admin.ModelAdmin):
    list_display = ('state', 'name', 'status')
    list_display_links = ("name",)
    search_fields = ("name", 'state')
    list_filter = ("status", 'state')


admin.site.register(City, CityAdmin)
