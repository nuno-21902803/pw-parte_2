# Generated by Django 3.2.3 on 2021-06-14 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20210614_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]