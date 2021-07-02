# Generated by Django 3.2.3 on 2021-07-02 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_auto_20210702_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_quizz',
            name='last_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='last', to='website.user_details'),
        ),
        migrations.AlterField(
            model_name='user_quizz',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first', to='website.user_details'),
        ),
    ]