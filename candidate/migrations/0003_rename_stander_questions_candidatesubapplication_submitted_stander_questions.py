# Generated by Django 4.1.5 on 2023-01-22 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0002_alter_candidatesubapplication_phase_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidatesubapplication',
            old_name='stander_questions',
            new_name='submitted_stander_questions',
        ),
    ]
