# Generated by Django 2.2.2 on 2019-06-25 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dbms', '0008_crop'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('land_name', models.CharField(max_length=20)),
                ('land_address', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=False)),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbms.Data')),
            ],
        ),
    ]