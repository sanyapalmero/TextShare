# Generated by Django 2.1.2 on 2019-01-10 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('code', '0007_auto_20181130_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='code',
            field=models.TextField(),
        ),
    ]