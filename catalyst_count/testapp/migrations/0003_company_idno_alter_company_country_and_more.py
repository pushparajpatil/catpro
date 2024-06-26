# Generated by Django 5.0.4 on 2024-04-24 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_alter_company_country_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='idno',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='company',
            name='country',
            field=models.CharField(default='india', max_length=255),
        ),
        migrations.AlterField(
            model_name='company',
            name='current_employee_estimate',
            field=models.PositiveIntegerField(default=786),
        ),
        migrations.AlterField(
            model_name='company',
            name='domain',
            field=models.CharField(default='sagar.com', max_length=255),
        ),
        migrations.AlterField(
            model_name='company',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='company',
            name='industry',
            field=models.CharField(default='Technology', max_length=255),
        ),
        migrations.AlterField(
            model_name='company',
            name='linkedin_url',
            field=models.URLField(default='default', max_length=255),
        ),
        migrations.AlterField(
            model_name='company',
            name='locality',
            field=models.CharField(default='dharangaon', max_length=255),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='company',
            name='size_range',
            field=models.CharField(default='not specified', max_length=50),
        ),
        migrations.AlterField(
            model_name='company',
            name='total_employee_estimate',
            field=models.PositiveIntegerField(default=786),
        ),
        migrations.AlterField(
            model_name='company',
            name='year_founded',
            field=models.PositiveIntegerField(default=2000),
        ),
    ]
