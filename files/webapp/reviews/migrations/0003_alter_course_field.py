# Generated by Django 4.1.4 on 2022-12-29 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='field',
            field=models.CharField(choices=[('Mathemathics', 'Mathemathics'), ('Statistics', 'Statistics'), ('Computer Science', 'Computer Science'), ('Economics and Finance', 'Economics and Finance'), ('Political Science', 'Political Science')], max_length=40),
        ),
    ]
