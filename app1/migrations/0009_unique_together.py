from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [("app_unique_together", "0002_auto_20190729_2122")]

    operations = [migrations.AlterUniqueTogether(name="a", unique_together=set())]