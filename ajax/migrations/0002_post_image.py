# Generated by Django 3.2.4 on 2021-06-11 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ajax', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to='upload'),
            preserve_default=False,
        ),
    ]
