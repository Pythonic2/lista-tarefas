# Generated by Django 5.0.7 on 2024-07-24 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_listatarefas_usuario_delete_pessoa_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='password',
            field=models.CharField(default='1234', max_length=128),
        ),
    ]
