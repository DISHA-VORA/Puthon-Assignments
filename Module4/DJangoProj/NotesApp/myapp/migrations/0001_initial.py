# Generated by Django 4.1.2 on 2022-11-02 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserSignUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('FName', models.CharField(max_length=20)),
                ('LName', models.CharField(max_length=20)),
                ('UNm', models.EmailField(max_length=254)),
                ('PWD', models.CharField(max_length=12)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('mobile', models.BigIntegerField()),
            ],
        ),
    ]
