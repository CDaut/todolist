# Generated by Django 3.2.9 on 2021-11-16 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('color', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('due_date', models.DateTimeField()),
                ('modifier_function', models.CharField(choices=[('e', 'exponential'), ('l', 'linear')], max_length=2)),
                ('importance', models.IntegerField()),
                ('urgency', models.IntegerField()),
                ('base_importance', models.IntegerField()),
                ('m', models.FloatField()),
                ('exponent', models.FloatField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.category')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.applicationuser')),
            ],
        ),
    ]
