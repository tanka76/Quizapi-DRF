# Generated by Django 3.1.3 on 2022-02-23 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer_text',
            field=models.TextField(verbose_name='Answer Text'),
        ),
    ]