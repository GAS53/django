# Generated by Django 4.0.4 on 2022-06-01 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_alter_customuser_age_alter_customuser_avatar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='age',
            field=models.SmallIntegerField(blank=True, null=True, verbose_name='age'),
        ),
    ]