# Generated by Django 5.0.1 on 2024-01-30 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noteapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='noteapp.tag'),
        ),
    ]