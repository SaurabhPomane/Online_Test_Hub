# Generated by Django 5.1.3 on 2024-11-30 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quetion',
            fields=[
                ('qno', models.IntegerField(primary_key=True, serialize=False)),
                ('gtext', models.CharField(max_length=50)),
                ('answer', models.CharField(max_length=50)),
                ('op1', models.CharField(max_length=50)),
                ('op2', models.CharField(max_length=50)),
                ('op3', models.CharField(max_length=50)),
                ('op4', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'quetions',
            },
        ),
    ]
