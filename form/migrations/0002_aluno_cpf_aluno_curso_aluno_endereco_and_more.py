# Generated by Django 4.1.3 on 2022-11-23 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='cpf',
            field=models.CharField(default='00000000000', max_length=11),
        ),
        migrations.AddField(
            model_name='aluno',
            name='curso',
            field=models.CharField(choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino')], max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='aluno',
            name='endereco',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='aluno',
            name='mini_curso',
            field=models.CharField(choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino')], max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='email',
            field=models.EmailField(max_length=150),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='sexo',
            field=models.CharField(choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino')], max_length=150, null=True),
        ),
    ]