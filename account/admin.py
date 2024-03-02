from django.contrib import admin
from .models import TreeCertificate

@admin.register(TreeCertificate)
class TreeCertificateAdmin(admin.ModelAdmin):
    list_display = ['certificate_type','planting_area','tree_quantity', 'tree_type', 'recipient_name', 'email']
    search_fields = ['recipient_name', 'email']
    list_filter = ['certificate_type', 'tree_type', 'planting_area']
    list_per_page = 20
