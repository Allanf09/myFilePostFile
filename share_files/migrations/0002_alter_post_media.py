# Generated by Django 3.2.3 on 2021-05-25 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share_files', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='media',
            field=models.FileField(upload_to='files'),
        ),
    ]
