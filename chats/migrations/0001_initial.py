# Generated by Django 4.2.4 on 2023-08-17 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=250, null=True)),
                ('sender', models.CharField(max_length=250)),
            ],
        ),
    ]
