# Generated by Django 4.2.3 on 2023-07-05 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0002_employee_bonus_employee_dept_employee_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='dept',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emp_app.department'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='hire_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emp_app.role'),
        ),
    ]
