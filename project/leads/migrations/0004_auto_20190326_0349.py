# Generated by Django 2.1.7 on 2019-03-26 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0003_auto_20190326_0213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]