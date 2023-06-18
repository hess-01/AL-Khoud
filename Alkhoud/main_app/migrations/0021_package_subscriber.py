# Generated by Django 4.2.2 on 2023-06-18 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0020_merge_20230618_1123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('details', models.TextField()),
                ('duration', models.CharField(max_length=200)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.club')),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(max_length=200)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.club')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.package')),
            ],
        ),
    ]