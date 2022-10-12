# Generated by Django 3.2.16 on 2022-10-11 22:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('prep_time', models.PositiveSmallIntegerField(blank=True, help_text='Enter time in minutes', null=True)),
                ('number_of_portions', models.PositiveIntegerField()),
                ('ingredients', models.TextField(help_text='One ingedient per line')),
                ('steps', models.TextField()),
                ('image', models.ImageField(blank=True, default='../default_post_swtmii', upload_to='images/')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]