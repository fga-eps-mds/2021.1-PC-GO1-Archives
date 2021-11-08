import csv
import sys
import os.path
import django
directory = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(directory)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()
from archives_app.fields_models import PublicWorker

csv.field_size_limit(sys.maxsize)

file_path = input("Caminho do arquivo de servidores: ")

with open(file_path) as f:
    csv_reader = csv.reader(f)
    try:
        for line in csv_reader:
            created = PublicWorker(
                name=line[0],
                cpf=line[1]
            )
            created.save()
    except Exception as e:
        print(e)
