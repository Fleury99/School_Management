# Generated by Django 4.1.7 on 2023-07-17 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Allocation', '0004_etudiant_tache_delete_projetouvert'),
    ]

    operations = [
        migrations.DeleteModel(
            name='InstructionsProjet',
        ),
        migrations.RemoveField(
            model_name='tache',
            name='instructeur',
        ),
        migrations.AddField(
            model_name='tache',
            name='matiere',
            field=models.CharField(default='Python', max_length=200),
        ),
        migrations.AlterField(
            model_name='tache',
            name='etudiant',
            field=models.ForeignKey(limit_choices_to={'role': 'etudiant'}, on_delete=django.db.models.deletion.CASCADE, to='Allocation.utilisateur'),
        ),
        migrations.DeleteModel(
            name='Etudiant',
        ),
    ]
