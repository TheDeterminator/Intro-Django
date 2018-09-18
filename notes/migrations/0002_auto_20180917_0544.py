# Generated by Django 2.1.1 on 2018-09-17 05:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='note',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]