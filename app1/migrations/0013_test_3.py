from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("app_drop_column", "0001_initial")]

    operations = [migrations.RemoveField(model_name="a", name="field_b")]