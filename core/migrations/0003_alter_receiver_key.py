# Generated by Django 4.1.5 on 2023-01-23 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_receiver_cpf_cnpj_alter_receiver_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receiver',
            name='key',
            field=models.CharField(max_length=250, verbose_name='Chave Pix'),
        ),
    ]
