# Generated by Django 3.2.3 on 2021-06-18 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_alter_user_details_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_details',
            name='email',
            field=models.CharField(default='xxx@soccernet.pt', max_length=50),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='phone',
            field=models.IntegerField(default=0),
        ),
    ]
