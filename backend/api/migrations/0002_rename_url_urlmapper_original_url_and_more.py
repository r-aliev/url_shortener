# Generated by Django 4.0 on 2022-11-07 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='urlmapper',
            old_name='url',
            new_name='original_url',
        ),
        migrations.RemoveField(
            model_name='urlmapper',
            name='hash',
        ),
        migrations.AddField(
            model_name='urlmapper',
            name='shortened_url_hash',
            field=models.CharField(default=1234567891, max_length=255),
            preserve_default=False,
        ),
    ]
