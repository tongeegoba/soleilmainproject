# Generated by Django 2.1.1 on 2019-01-26 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20190126_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='other_authors',
            field=models.CharField(blank=True, default='0', max_length=300, null=True),
        ),
    ]
