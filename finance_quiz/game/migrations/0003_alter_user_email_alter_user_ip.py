# Generated by Django 4.1.3 on 2022-12-04 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_user_ip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='ip',
            field=models.CharField(max_length=39),
        ),
    ]
