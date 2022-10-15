# Generated by Django 4.1.1 on 2022-10-12 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0009_perfil'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Serie',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
        migrations.AddField(
            model_name='publi',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='publicaciones'),
        ),
        migrations.AlterField(
            model_name='avatar',
            name='imagen',
            field=models.ImageField(blank=True, default='blank-profile-picture.png', null=True, upload_to='avatares'),
        ),
    ]
