# Generated by Django 4.1.4 on 2022-12-27 17:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.doctor'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='patient',
            name='time',
            field=models.CharField(choices=[('3    PM', ' 3    PM'), ('3:30 PM', ' 3:30 PM'), ('4    PM', ' 4    PM'), ('4:30 PM', ' 4:30 PM'), ('5    PM', ' 5    PM'), ('5:30 PM', ' 5:30 PM'), ('6    PM', ' 6    PM'), ('6:30 PM', ' 6:30 PM'), ('7    PM', ' 7    PM')], max_length=100),
        ),
    ]
