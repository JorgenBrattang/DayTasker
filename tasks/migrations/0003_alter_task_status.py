# Generated by Django 3.2.16 on 2022-11-14 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('not_done', 'Not Done'), ('in_progress', 'In Progress'), ('done', 'Done')], default='not_done', max_length=50),
        ),
    ]
