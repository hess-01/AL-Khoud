# Generated by Django 4.2.2 on 2023-06-14 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_rename_expert_coach_experience_club_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(default='images/default.jpg', upload_to='images/')),
                ('decription', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='club',
            name='type',
        ),
        migrations.AddField(
            model_name='club',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main_app.category'),
        ),
    ]