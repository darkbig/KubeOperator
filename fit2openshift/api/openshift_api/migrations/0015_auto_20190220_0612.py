# Generated by Django 2.1.2 on 2019-02-20 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('openshift_api', '0014_auto_20190220_0326'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='host',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='host', to='openshift_api.Host'),
        ),
        migrations.AlterField(
            model_name='host',
            name='node',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='node', to='openshift_api.Node'),
        ),
    ]
