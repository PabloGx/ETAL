# Generated by Django 4.1.3 on 2022-11-24 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_aluno_cpf_aluno_curso_aluno_endereco_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='mini_curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
            ],
        ),
        migrations.AlterField(
            model_name='aluno',
            name='curso',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.RemoveField(
            model_name='aluno',
            name='mini_curso',
        ),
        migrations.AlterField(
            model_name='aluno',
            name='sexo',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='aluno',
            name='mini_curso',
            field=models.ManyToManyField(to='form.mini_curso'),
        ),
    ]
