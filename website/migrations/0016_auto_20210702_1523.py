# Generated by Django 3.2.3 on 2021-07-02 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_alter_user_details_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizz',
            name='user_id_quizz',
        ),
        migrations.CreateModel(
            name='User_Quizz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('quizzes', models.ManyToManyField(blank=True, related_name='QuizzesUser', to='website.Quizz')),
            ],
        ),
    ]
