# Generated by Django 4.1.5 on 2023-01-15 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0008_candidate_vote1_candidate_vote3_candidate_vote5'),
        ('users', '0009_user_events_user_organised_events'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='vote1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='voter12', to='elections.candidate'),
        ),
        migrations.AddField(
            model_name='user',
            name='vote2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='voter23', to='elections.candidate'),
        ),
        migrations.AddField(
            model_name='user',
            name='vote3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='voter31', to='elections.candidate'),
        ),
    ]
