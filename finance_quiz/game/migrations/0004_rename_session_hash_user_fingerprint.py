# Generated by Django 4.1.3 on 2022-12-09 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_alter_user_session_hash'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='session_hash',
            new_name='fingerprint',
        ),
    ]