import pandas as pd
from django.core.management.base import BaseCommand
from testapp.models import Company  
#from . import companies_sorted


class Command(BaseCommand):
    help = 'Import data from CSV file to MySQL database'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        df = pd.read_csv("D://catpro//catalyst_count//testapp//management//commands//companies_sorted.csv")
        for index, row in df.iterrows():
            Company.objects.create(
                idno=row['idno'],
                name=row['name'],
                domain=row['domain'],
                year_founded=row['year founded'],
                industry=row['industry'],
                size_range=row['size range'],
                locality=row['locality'],
                country=row['country'],
                linkedin_url=row['linkedin url'],
                current_employee_estimate=row['current employee estimate'],
                total_employee_estimate=row['total employee estimate']
            )

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))