# Generated by Django 4.1.7 on 2023-07-15 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjetArchive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intitule', models.CharField(max_length=200)),
                ('matiere', models.CharField(max_length=200)),
                ('fichier_projet', models.FileField(upload_to='projets/')),
                ('statut', models.CharField(choices=[('en_cours', 'En cours'), ('soumis', 'Soumis'), ('corrigé', 'Corrigé'), ('traité', 'Traité'), ('archivé', 'Archivé')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('date_naissance', models.DateField()),
                ('numero_etudiant_enseignant', models.CharField(max_length=20)),
                ('role', models.CharField(choices=[('etudiant', 'Étudiant'), ('enseignant', 'Enseignant'), ('administrateur', 'Administrateur')], max_length=20)),
                ('identifiant', models.CharField(max_length=100)),
                ('mot_de_passe', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProjetOuvert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intitule', models.CharField(max_length=200)),
                ('matiere', models.CharField(max_length=200)),
                ('fichier_projet', models.FileField(upload_to='projets/')),
                ('statut', models.CharField(choices=[('en_cours', 'En cours'), ('soumis', 'Soumis'), ('corrigé', 'Corrigé'), ('traité', 'Traité'), ('archivé', 'Archivé')], max_length=20)),
                ('instructeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Allocation.utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='Projet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intitule', models.CharField(max_length=200)),
                ('matiere', models.CharField(max_length=200)),
                ('fichier_projet', models.FileField(upload_to='projets/')),
                ('statut', models.CharField(choices=[('en_cours', 'En cours'), ('soumis', 'Soumis'), ('corrigé', 'Corrigé'), ('traite', 'Traité'), ('archive', 'Archivé')], max_length=20)),
                ('notes_avis', models.TextField(blank=True)),
                ('instructeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Allocation.utilisateur')),
            ],
        ),
    ]
