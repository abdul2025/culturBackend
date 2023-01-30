# Generated by Django 4.1.5 on 2023-01-30 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_customuser_options_alter_customuser_managers_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loginlog',
            name='username',
        ),
        migrations.AddField(
            model_name='loginlog',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]