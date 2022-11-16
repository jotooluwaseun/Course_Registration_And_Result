# Generated by Django 4.1.3 on 2022-11-08 23:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('code', models.CharField(blank=True, max_length=15, null=True)),
                ('credits', models.IntegerField(blank=True, null=True)),
                ('level', models.CharField(blank=True, choices=[('300', '300'), ('400', '400'), ('500', '500')], max_length=3, null=True)),
                ('semester', models.CharField(blank=True, choices=[('First', 'First'), ('Second', 'Second')], max_length=20, null=True)),
                ('status', models.CharField(blank=True, choices=[('C', 'C'), ('R', 'R'), ('E', 'E')], max_length=20, null=True)),
            ],
            options={
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('code', models.CharField(blank=True, max_length=15, null=True)),
                ('faculty', models.CharField(blank=True, choices=[('Science', 'Science')], max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'Departments',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matric_no', models.CharField(blank=True, max_length=150, null=True, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=150, null=True)),
                ('last_name', models.CharField(blank=True, max_length=150, null=True)),
                ('email', models.EmailField(blank=True, max_length=255, null=True, unique=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6, null=True)),
                ('entry_date', models.DateField(blank=True, null=True)),
                ('graduated_date', models.DateField(blank=True, null=True)),
                ('program', models.CharField(blank=True, choices=[('Part-Time', 'Part-Time'), ('HND Conversion', 'HND Conversion')], default='HND Conversion', max_length=150, null=True)),
                ('cgpa', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=3, null=True)),
                ('status', models.CharField(blank=True, choices=[('In Progress', 'In Progress'), ('Completed', 'Completed')], default='In Progress', max_length=20, null=True)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='academics.department')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Students',
            },
        ),
        migrations.CreateModel(
            name='StudentGrade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(blank=True, choices=[('300', '300'), ('400', '400'), ('500', '500')], max_length=3, null=True)),
                ('semester', models.CharField(blank=True, choices=[('First', 'First'), ('Second', 'Second')], max_length=20, null=True)),
                ('gpa', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('status', models.CharField(blank=True, choices=[('In Progress', 'In Progress'), ('Completed', 'Completed')], max_length=20, null=True)),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='academics.student')),
            ],
            options={
                'verbose_name_plural': 'Student Grades',
            },
        ),
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, choices=[('Mr.', 'Mr.'), ('Mrs.', 'Mrs.'), ('Ms.', 'Ms.'), ('Dr.', 'Dr.'), ('Prof.', 'Prof.')], max_length=10, null=True)),
                ('first_name', models.CharField(blank=True, max_length=200, null=True)),
                ('last_name', models.CharField(blank=True, max_length=200, null=True)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='academics.department')),
            ],
            options={
                'verbose_name_plural': 'Lecturers',
            },
        ),
        migrations.CreateModel(
            name='CourseRegistrationAndResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_score', models.PositiveIntegerField(blank=True, null=True)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='academics.course')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='academics.student')),
            ],
            options={
                'verbose_name_plural': 'Course Registration and Results',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='academics.department'),
        ),
        migrations.AddField(
            model_name='course',
            name='lecturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='academics.lecturer'),
        ),
    ]
