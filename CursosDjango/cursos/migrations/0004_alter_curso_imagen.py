# Generated by Django 5.0.6 on 2025-06-30 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0003_alter_curso_options_curso_fecha_modificacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='imagen',
            field=models.ImageField(null=True, upload_to='fotos', verbose_name='img'),
        ),
    ]
