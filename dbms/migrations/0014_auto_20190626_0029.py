# Generated by Django 2.2.2 on 2019-06-26 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbms', '0013_auto_20190626_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='accepted',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False'), ('Pending', 'Pending')], default='Pending', max_length=7),
        ),
    ]