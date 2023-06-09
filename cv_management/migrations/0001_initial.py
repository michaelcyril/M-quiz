# Generated by Django 4.2.1 on 2023-06-04 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=200)),
                ('is_correct', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'answer',
            },
        ),
        migrations.CreateModel(
            name='Attempts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percent', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'attempts',
            },
        ),
        migrations.CreateModel(
            name='JobVacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=30)),
                ('jobTitle', models.CharField(max_length=200)),
                ('jobType', models.CharField(choices=[('part-time', 'part-time'), ('full-time', 'full-time')], max_length=20)),
            ],
            options={
                'db_table': 'job_vacancy',
            },
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requirement', models.CharField(max_length=200)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cv_management.jobvacancy')),
            ],
            options={
                'db_table': 'requirements',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('is_checkable', models.BooleanField(default=False)),
                ('vacancy_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cv_management.jobvacancy')),
            ],
            options={
                'db_table': 'question',
            },
        ),
    ]
