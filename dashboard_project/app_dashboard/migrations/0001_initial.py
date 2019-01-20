# Generated by Django 2.1.3 on 2019-01-21 01:47

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
            name='EmployeeDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_no', models.IntegerField(max_length=10, verbose_name='Phone Number')),
                ('pan_no', models.CharField(max_length=10, verbose_name='PAN No')),
                ('adhaar_no', models.CharField(max_length=10, verbose_name='Adhaar No')),
                ('dob', models.DateField(verbose_name='Date Of Birth')),
                ('skill_proficiency', models.DecimalField(decimal_places=1, default=0, max_digits=5, verbose_name='Skill Proficiency (Specify in Years.Months Format)')),
                ('comment', models.TextField(blank=True, default='', max_length=50, verbose_name='Comments')),
                ('employee_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SkillSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=50, unique=True, verbose_name='Skills')),
                ('skill_version', models.CharField(max_length=10, verbose_name='Version Used')),
            ],
        ),
        migrations.AddField(
            model_name='employeedetails',
            name='skills',
            field=models.ManyToManyField(to='app_dashboard.SkillSet', verbose_name='Skills'),
        ),
    ]
