import datetime

from nem_records.models import AccumulationRecord, HeaderRecord


def get_csv_data(csv_reader, header_record, file_path):
    rows = []
    for row in csv_reader:
        if row[1] and row[6] and row[18] and row[14]:
            reading_date = datetime.datetime.strptime(row[14], "%Y%m%d%H%M%S")

            meter_reading = row[18] if row[18] else 0.0
            rows.append(
                AccumulationRecord(
                    header_record=header_record,
                    nmi=row[1],
                    meter_serial_number=row[6],
                    meter_reading_value=meter_reading,
                    reading_date=reading_date,
                )
            )
    return rows


def check_file_extension(file_path):
    return True if file_path.endswith(".csv") else False


def create_header_record(file_path, raw_data=[]):
    file_name = file_path.split("/")[-1]
    reading_date = datetime.datetime.strptime(raw_data[2], "%Y%m%d%H%M%S")

    header_record, _ = HeaderRecord.objects.get_or_create(
        file_name=file_name,
        record_indicator=raw_data[0],
        nem_version=raw_data[1],
        date_time=reading_date,
        from_participant=raw_data[3],
        to_participant=raw_data[4],
    )
    return header_record
