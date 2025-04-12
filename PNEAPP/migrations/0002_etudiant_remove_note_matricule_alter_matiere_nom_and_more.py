# Generated by Django 5.1.7 on 2025-04-06 02:33

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PNEAPP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='note',
            name='matricule',
        ),
        migrations.AlterField(
            model_name='matiere',
            name='nom',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='note',
            name='date_saisie',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='note',
            name='mention',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='note',
            name='note',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='note',
            name='etudiant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PNEAPP.etudiant'),
        ),
    ]
