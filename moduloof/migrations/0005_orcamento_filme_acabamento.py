# Generated by Django 2.1.5 on 2019-03-19 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moduloof', '0004_remove_orcamento_filme_acabamento'),
    ]

    operations = [
        migrations.AddField(
            model_name='orcamento_filme',
            name='acabamento',
            field=models.ForeignKey(default=0, on_delete='cascade', to='moduloof.Acabamento'),
            preserve_default=False,
        ),
    ]
