from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("app_rename_column", "0001_initial")]

    operations = [
        migrations.RenameField(model_name="a", old_name="field", new_name="renamed")
    ]