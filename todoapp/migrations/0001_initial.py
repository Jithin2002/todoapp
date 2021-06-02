# Generated by Django 3.2.3 on 2021-05-29 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=150)),
                ('status', models.CharField(default='not completed', max_length=15)),
                ('user', models.CharField(max_length=140)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]
