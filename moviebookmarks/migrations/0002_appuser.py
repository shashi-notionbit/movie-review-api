# Generated by Django 2.2.6 on 2019-10-12 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviebookmarks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
