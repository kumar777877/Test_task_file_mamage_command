from django.db import models


class HeaderRecord(models.Model):
    file_name = models.CharField(max_length=50)
    record_indicator = models.IntegerField()
    nem_version = models.CharField(max_length=10)
    date_time = models.DateTimeField()
    from_participant = models.CharField(max_length=10)
    to_participant = models.CharField(max_length=10)

    def __str__(self):
        return self.file_name


class AccumulationRecord(models.Model):
    header_record = models.ForeignKey(HeaderRecord, on_delete=models.CASCADE)
    nmi = models.CharField(max_length=10)
    meter_serial_number = models.CharField(max_length=12)
    meter_reading_value = models.DecimalField(max_digits=8, decimal_places=2)
    reading_date = models.DateTimeField()

    def __str__(self):
        return self.meter_serial_number
