# Generated by Django 4.0.6 on 2022-07-29 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0003_rename_name_expensemodel_expense_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensemodel',
            name='expense',
            field=models.CharField(max_length=30),
        ),
    ]
