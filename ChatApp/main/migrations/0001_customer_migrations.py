from django.db import migrations
from django.contrib.postgres.operations import TrigramExtension


class Migration(migrations.Migration):
    ''' Activate the pg_trgm extension on PostgreSQL '''
    dependencies = []

    operations = [
        TrigramExtension(),
    ]