# Generated by Django 2.2.2 on 2019-06-22 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dbms', '0002_auto_20190620_1846'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='id',
        ),
        migrations.AlterField(
            model_name='data',
            name='user_name',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Lands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('land_name', models.CharField(max_length=100)),
                ('land_add', models.CharField(max_length=100)),
                ('crop_grown', models.CharField(max_length=100)),
                ('moisture_req', models.IntegerField(default=0)),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbms.Data')),
            ],
        ),
    ]
