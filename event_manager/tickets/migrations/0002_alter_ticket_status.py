# Generated by Django 4.2.2 on 2023-06-23 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('option1', 'Option 1'), ('option2', 'Option 2')], max_length=10),
        ),
    ]
