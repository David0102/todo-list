# Generated by Django 5.1.1 on 2024-09-24 01:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tarefas", "0009_alter_tarefa_data_criacao"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tarefa",
            name="data_criacao",
            field=models.DateField(auto_now_add=True, verbose_name="Criado em"),
        ),
    ]
