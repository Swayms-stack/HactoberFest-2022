# Generated by Django 3.0.5 on 2022-09-29 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Desk', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='count_in_library',
            field=models.IntegerField(blank=True, default=10),
        ),
        migrations.AlterField(
            model_name='author',
            name='address',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
