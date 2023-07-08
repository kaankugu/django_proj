# Generated by Django 4.2.2 on 2023-06-23 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mvt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mainmenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menucode', models.ImageField(upload_to='')),
                ('menuname', models.CharField(max_length=100)),
                ('menutype', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='MenuList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menucode', models.ImageField(upload_to='')),
                ('menuname', models.CharField(max_length=100)),
                ('menutype', models.ImageField(upload_to='')),
                ('submenuname', models.CharField(max_length=100)),
                ('menulink', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
