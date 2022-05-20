class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Model1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="a",
            name="new_not_null_field",
            field=models.IntegerField(default=1),
            preserve_default=False,
        )
    ]

    operations = [
        migrations.AddField(
            model_name="a", name="not_null_field", field=models.IntegerField(default=1)
        ),
        AddDefaultValue(model_name="a", name="not_null_field", value=1),
    ]

    operations = [
        migrations.AlterField(
            model_name="a",
            name="field",
            field=models.CharField(max_length=10, null=True),
        )
    ]

    operations = [migrations.RemoveField(model_name="a", name="field_b")]

    operations = [migrations.DeleteModel(name="A")]

    operations = [
        migrations.RenameField(model_name="a", old_name="field", new_name="renamed")
    ]

    operations = [migrations.RenameModel(old_name="A", new_name="B")]

    operations = [migrations.AlterUniqueTogether(name="a", unique_together=set())]