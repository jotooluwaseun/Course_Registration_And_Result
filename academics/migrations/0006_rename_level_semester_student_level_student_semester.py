# Generated by Django 4.1.3 on 2022-11-13 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0005_student_level_semester'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='level_semester',
            new_name='level',
        ),
        migrations.AddField(
            model_name='student',
            name='semester',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]