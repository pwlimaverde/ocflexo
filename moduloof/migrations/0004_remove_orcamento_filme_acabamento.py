# Generated by Django 2.1.5 on 2019-03-19 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moduloof', '0003_orcamento_filme_acabamento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orcamento_filme',
            name='acabamento',
        ),
    ]
