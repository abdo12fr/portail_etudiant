<<<<<<< HEAD
# Generated by Django 5.1.7 on 2025-04-06 02:16

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models
=======
# Generated by Django 4.2 on 2025-04-18 17:30

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
>>>>>>> 912d90e (Initial commit)


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
<<<<<<< HEAD
=======
            name='Etudiant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
>>>>>>> 912d90e (Initial commit)
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('nom', models.CharField(max_length=100, unique=True)),
=======
                ('nom', models.CharField(max_length=100)),
>>>>>>> 912d90e (Initial commit)
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
<<<<<<< HEAD
                ('role', models.CharField(choices=[('etudiant', 'Étudiant'), ('prof', 'Professeur')], default='etudiant', max_length=50)),
=======
                ('role', models.CharField(choices=[('Prof', 'Professeur'), ('etudiant', 'Étudiant')], default='etudiant', max_length=20)),
>>>>>>> 912d90e (Initial commit)
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricule', models.CharField(blank=True, max_length=20, null=True)),
                ('classe', models.CharField(blank=True, max_length=50, null=True)),
                ('ecole', models.CharField(blank=True, max_length=100, null=True)),
                ('groupe', models.CharField(blank=True, max_length=50, null=True)),
                ('numerocne', models.CharField(blank=True, max_length=20, null=True)),
                ('sexe', models.CharField(blank=True, choices=[('M', 'Masculin'), ('F', 'Féminin')], max_length=10, null=True)),
                ('date_naissance', models.DateField(blank=True, null=True)),
                ('nationalite', models.CharField(blank=True, max_length=50, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('note', models.FloatField()),
                ('mention', models.CharField(choices=[('TB', 'Très Bien'), ('B', 'Bien'), ('AB', 'Assez Bien'), ('P', 'Passable'), ('I', 'Insuffisant')], max_length=50)),
                ('date_saisie', models.DateTimeField(auto_now_add=True)),
                ('matricule', models.CharField(max_length=20, unique=True)),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PNEAPP.matiere')),
                ('etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
=======
                ('note', models.DecimalField(decimal_places=2, max_digits=4)),
                ('mention', models.CharField(choices=[('TB', 'Très Bien'), ('B', 'Bien'), ('AB', 'Assez Bien'), ('P', 'Passable'), ('I', 'Insuffisant')], max_length=2)),
                ('valeur', models.DecimalField(decimal_places=2, max_digits=5)),
                ('etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PNEAPP.matiere')),
>>>>>>> 912d90e (Initial commit)
            ],
        ),
    ]
