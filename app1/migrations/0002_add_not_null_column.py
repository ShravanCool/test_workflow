from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("app_add_not_null_column", "0001_create_table")]

    operations = [
        migrations.AddField(
            model_name="a",
            name="new_not_null_field",
            field=models.IntegerField(default=1),
            preserve_default=False,
        )
    ]