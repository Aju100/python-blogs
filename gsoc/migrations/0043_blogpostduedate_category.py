# Generated by Django 2.1.9 on 2019-07-07 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gsoc', '0042_auto_20190707_0505'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpostduedate',
            name='category',
            field=models.IntegerField(blank=True, choices=[(0, 'Weekly Check-In'), (1, 'Blog Post')], null=True),
        ),
    ]