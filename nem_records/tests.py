import io
import os
from io import StringIO

from django.core import management
from django.test import TestCase


class ImportCsvFilesTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super(ImportCsvFilesTests, cls).setUpClass()
        base_path = os.getcwd()
        cls.file_path = os.path.join(
            base_path, "nem_records/fixture/", "data.csv"
            )
        cls.invalid_csv_path = os.path.join(
            base_path, "nem_records/fixture/", "invalid_data.csv"
        )
        cls.filetype = os.path.join(
            base_path, "nem_records/fixture/", "invalid_filetype.txt"
        )
        cls.emptyfile = os.path.join(
            base_path, "nem_records/fixture/", "empty.csv"
            )

    def test_with_valid_csv_file(self):
        out = io.StringIO()
        opts = {"url": [self.file_path]}
        management.call_command("import_meterdata", **opts, stdout=out)
        self.assertEqual(
            out.getvalue().strip(),
             f"File: {self.file_path} processed"
             )

    def test_with_wrong_csv_path(self):
        out = StringIO()

        with self.assertRaises(FileNotFoundError):
            opts = {"url": ["/octopus/data.csv"]}
            management.call_command(
                "import_meterdata", **opts, stdout=out
                )

    def test_with_other_filetype(self):
        out = StringIO()
        with self.assertRaises(TypeError):
            opts = {"url": [self.filetype]}
            management.call_command(
                "import_meterdata", **opts, stdout=out
                )

    def test_with_no_data(self):
        out = StringIO()
        with self.assertRaises(Exception):
            opts = {"url": [self.emptyfile]}
            management.call_command(
                "import_meterdata", **opts, stdout=out
                )
