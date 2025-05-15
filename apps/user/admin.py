# django
from django.contrib import admin
# third
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# own
from apps.user.models import UserApp

# Register your models here.

class UserResource(resources.ModelResource):
	class Meta:
		model = UserApp

class UserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	search_fields = ("name", "last_name", "usuid", "rol")
	list_display = ("name", "last_name", "usuid", "rol")
	list_filter = ("usuid", "rol")
	readonly_fields = ('created_at', 'update_at')
	ordering = ['name']
	resource_class = UserResource

admin.site.register(UserApp, UserAdmin)