# Generated by Django 3.0.4 on 2020-03-17 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contact_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='Contact_id',
            field=models.ForeignKey(db_column='Contact_id', on_delete=django.db.models.deletion.CASCADE, to='contact_app.Contact'),
        ),
        migrations.AlterField(
            model_name='date',
            name='Contact_id',
            field=models.ForeignKey(db_column='Contact_id', on_delete=django.db.models.deletion.CASCADE, to='contact_app.Contact'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='Contact_id',
            field=models.ForeignKey(db_column='Contact_id', on_delete=django.db.models.deletion.CASCADE, to='contact_app.Contact'),
        ),
    ]