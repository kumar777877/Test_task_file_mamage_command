import csv
import os

from django.core.management.base import BaseCommand

from nem_records.models import AccumulationRecord
from nem_records import utils


class Command(BaseCommand):
    """
    This management command takes csv file path as argument.
    And reads the data from it and saves into the database.
    """

    help = "Import .csv file into models"

    def add_arguments(self, parser):
        parser.add_argument(
            "--url",
            action="append",
            type=str,
            help="Import csv file to database.",
        )

    def handle(self, *args, **options):

        url = options.get("url")
        file_path = url[0] if url else ""
        if file_path and not os.path.exists(file_path):
            raise FileNotFoundError(f"File: {file_path}")

        if not utils.check_file_extension(file_path):
            raise TypeError(
                "only a csv file can be processed"
                )

        with open(file_path, "rt") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",", quotechar='"')
            header_line = next(csv_reader)
            header_instance = utils.create_header_record(
                file_path, header_line
                )

            csv_data = utils.get_csv_data(
                csv_reader, header_instance, file_path
                )
            if not csv_data:
                raise Exception(f"data not found in the file : {file_path}")

            AccumulationRecord.objects.bulk_create(csv_data)
        self.stdout.write(f"File: {file_path} processed ")
