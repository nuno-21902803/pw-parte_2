# Generated by Django 3.2.3 on 2021-06-26 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_alter_user_quizz_quizzes'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Opinion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.IntegerField(default=0)),
                ('opinion_text', models.CharField(max_length=300)),
                ('opinion2', models.IntegerField(default=0)),
                ('opinion3', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='user_quizz',
            name='quizzes',
            field=models.ManyToManyField(blank=True, related_name='QuizzesUser', to='website.Quizz'),
        ),
    ]
