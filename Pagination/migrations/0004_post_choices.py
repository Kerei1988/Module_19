# Generated by Django 5.1 on 2024-09-15 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pagination', '0003_remove_post_choices'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='choices',
            field=models.CharField(choices=[(1, '1 элемент'), (2, '2 элемента'), (3, '3 элемента')], default=1, max_length=1),
        ),
    ]
