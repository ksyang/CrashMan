# Generated by Django 2.0.6 on 2018-06-06 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Docker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Docker_Name', models.CharField(max_length=30)),
                ('Program', models.CharField(max_length=30)),
                ('Fuzzer', models.CharField(default='afl', max_length=30)),
                ('Port', models.CharField(max_length=10)),
            ],
        ),
    ]