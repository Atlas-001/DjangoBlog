# Generated by Django 4.1.1 on 2022-10-15 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0012_alter_post_options_alter_post_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='anio',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='genero',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='titulo',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
