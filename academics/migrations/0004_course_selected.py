# Generated by Django 4.1.3 on 2022-11-12 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0003_alter_student_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='selected',
            field=models.BooleanField(default=True),
        ),
    ]