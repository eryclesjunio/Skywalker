# Generated by Django 2.0.2 on 2018-08-06 01:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skywalker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=1200)),
                ('password', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skywalker.User'),
        ),
    ]