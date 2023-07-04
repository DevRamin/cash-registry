# Generated by Django 4.2.3 on 2023-07-04 19:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("registry", "0002_delete_greeting_alter_registry_default_messages"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="registry",
            name="default_messages",
        ),
        migrations.AddField(
            model_name="occasion",
            name="default_messages",
            field=models.ManyToManyField(blank=True, to="registry.defaultmessage"),
        ),
    ]