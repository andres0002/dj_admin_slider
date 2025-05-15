# django
from django.contrib import admin
# third
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# own
from apps.slider.models import Slider

# Register your models here.

class SliderResource(resources.ModelResource):
	class Meta:
		model = Slider

class SliderAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	search_fields = ("slug", "image", "created_at", "updated_at")
	list_display = ("slug", "image", "created_at", "updated_at")
	list_filter = ( "created_at", "updated_at")
	resource_class = SliderResource

admin.site.register(Slider, SliderAdmin)