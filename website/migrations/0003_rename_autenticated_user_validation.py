# Generated by Django 3.2.3 on 2021-06-11 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_user_autenticated'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='autenticated',
            new_name='validation',
        ),
    ]
