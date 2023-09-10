from django.contrib import admin
from .models import CuboidBox

@admin.register(CuboidBox)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id','creator','length', 'breadth', 'height','area', 'volume','created_at','updated_at']
    
    list_per_page = 10
    
    
    
    def has_delete_permission(self, request, obj=None):
            if obj is not None and obj.user == request.user:
                return True
            return False

    
   