# Generated by Django 2.0.2 on 2018-08-08 03:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skywalker', '0003_auto_20180805_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turma',
            name='responsavel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]