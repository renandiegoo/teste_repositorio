# Generated by Django 5.0.1 on 2024-01-18 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aaaa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='imagens_produtos/'),
        ),
    ]
