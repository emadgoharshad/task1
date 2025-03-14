# Generated by Django 5.1.7 on 2025-03-13 07:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_rename_stat_time_songsinger_start_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='type',
            new_name='genre',
        ),
        migrations.AlterField(
            model_name='album',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='song',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='songsinger',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='song_singers', to='music.song'),
        ),
    ]
