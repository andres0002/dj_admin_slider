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
	search_fields = ("slug", "image", "create_date", "update_date")
	list_display = ("slug", "image", "create_date", "update_date")
	list_filter = ( "create_date", "update_date")
	resource_class = SliderResource

admin.site.register(Slider, SliderAdmin)