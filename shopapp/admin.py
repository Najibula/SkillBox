from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest
from .admin_mixins import ExportAsCSVMixin

from .models import Products, Order

class OrderInline(admin.TabularInline):
    extra = 0
    model = Products.orders.through


@admin.action(description="Archived products")
def merk_archived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=True)

@admin.action(description="Unarchived products")
def merk_unarchived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=False)

@admin.register(Products)
class ProdactAdmin(admin.ModelAdmin, ExportAsCSVMixin):
    actions = [
        merk_archived,
        merk_unarchived,
        "export_csv",
    ]
    inlines = [
        OrderInline,
    ]
    #list_display = "pk","name","description","price","discount"
    list_display = "pk", "name", "description_short", "price", "discount","archived"
    list_display_links = "pk","name"
    ordering = "-name","pk"
    search_fields = "name","description"
    fieldsets = [
        (None,{
            "fields": ("name","description")
        }),
        ("Price options",{
            "fields": ("price","discount"),
            "classes": ("wide","collapse"),
        }),
        ("Extra options",{
            "fields": ("archived",),
            "classes": ("collapse",),
            "description": "EXtra options. Field 'archived' is for soft delete",
        })
    ]

    def description_short(self, obj: Products) -> str:
        if len(obj.description) < 48 :
            return obj.description
        return obj.description[:48]+"..."
    description_short.short_description = "My Custom Field"




#class ProductsInLine(admin.TabularInline):
class ProductsInLine(admin.StackedInline):
    extra = 0
    model = Order.products.through

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        ProductsInLine,
    ]
    list_display = "delivery_address","promocode","created_at","user_verbose"

    def get_queryset(self, request):
        return Order.objects.select_related("user").prefetch_related("products")

    def user_verbose(self,obj:Order):
        return obj.user.first_name or obj.user.username


#admin.site.register(Products,ProdactAdmin)