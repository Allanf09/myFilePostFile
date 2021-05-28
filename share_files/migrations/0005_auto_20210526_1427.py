# Generated by Django 3.2.3 on 2021-05-26 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share_files', '0004_auto_20210525_1643'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={},
        ),
        migrations.RemoveField(
            model_name='post',
            name='comment',
        ),
        migrations.AddField(
            model_name='post',
            name='posted_by',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]