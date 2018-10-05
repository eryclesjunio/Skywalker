# Generated by Django 2.0.2 on 2018-08-09 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skywalker', '0006_remove_turma_quantidade_alunos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skywalker.User')),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skywalker.Turma')),
            ],
        ),
    ]