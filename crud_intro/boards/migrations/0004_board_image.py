# Generated by Django 2.2.2 on 2019-06-12 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
