# Generated by Django 4.2.1 on 2023-05-24 20:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("prose", "0002_alter_document_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="document",
            name="title",
            field=models.TextField(
                blank=True, max_length=200, verbose_name="Title for this Document"
            ),
        ),
    ]
