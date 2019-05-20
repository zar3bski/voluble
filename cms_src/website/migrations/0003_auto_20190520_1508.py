# Generated by Django 2.2 on 2019-05-20 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20190518_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='language',
            field=models.CharField(choices=[('fr', 'French'), ('en', 'English'), ('es', 'Spanish')], default='en', max_length=1),
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.CharField(help_text='comma separated tags', max_length=100),
        ),
        migrations.AlterField(
            model_name='certification',
            name='expire',
            field=models.DateField(blank=True, null=True),
        ),
    ]
