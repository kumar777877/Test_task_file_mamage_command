from django.contrib import admin

from nem_records import models


class HeaderRecordAdmin(admin.ModelAdmin):
    list_display = (
        "record_indicator",
        "nem_version",
        "date_time",
        "from_participant",
        "to_participant",
    )


class AccumulationRecordAdmin(admin.ModelAdmin):
    list_display = (
        "header_record",
        "nmi",
        "meter_serial_number",
        "meter_reading_value",
        "reading_date",
    )
    search_fields = ("nmi", "meter_serial_number")


admin.site.register(models.AccumulationRecord, AccumulationRecordAdmin)
admin.site.register(models.HeaderRecord, HeaderRecordAdmin)
        