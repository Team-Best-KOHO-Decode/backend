# Generated by Django 3.2.7 on 2021-09-23 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='name',
            field=models.CharField(default='NONE', max_length=100),
            preserve_default=False,
        ),
    ]
