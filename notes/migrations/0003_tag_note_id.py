# Generated by Django 2.1.1 on 2018-09-17 06:09

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20180917_0544'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='note_id',
            field=models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, to='notes.Note'),
        ),
    ]
