# Generated by Django 4.2 on 2025-04-10 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PNEAPP', '0005_alter_note_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='role',
            field=models.CharField(choices=[('etudiant', 'Etudiant'), ('prof', 'Prof')], default=1, max_length=50),
            preserve_default=False,
        ),
    ]
