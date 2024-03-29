# Generated by Django 4.2.1 on 2024-01-23 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_code', models.CharField(max_length=10)),
                ('field_code', models.CharField(max_length=10)),
                ('hall_ticket', models.CharField(max_length=10)),
                ('marks', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=255)),
                ('backlogs', models.TextField()),
            ],
        ),
    ]
