# Generated by Django 4.1.1 on 2022-10-03 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoApp', '0003_alter_boss_your_todo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boss',
            name='your_todo',
            field=models.CharField(max_length=60),
        ),
    ]
