# Generated by Django 5.1.1 on 2024-09-24 01:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tarefas", "0008_alter_tarefa_table"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tarefa",
            name="data_criacao",
            field=models.DateField(verbose_name="Criado em"),
        ),
    ]
