from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("app_alter_column", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="a",
            name="field",
            field=models.CharField(max_length=10, null=True),
        )
    ]