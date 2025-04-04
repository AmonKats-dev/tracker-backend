# Generated by Django 5.1.7 on 2025-03-25 13:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('academic', '0002_initial'),
        ('issues', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='attachment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='category',
            name='college',
            field=models.ForeignKey(blank=True, help_text='Null for global categories', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categories', to='academic.college'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='issue',
            name='assignee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_issues', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='issue',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='issues', to='issues.category'),
        ),
        migrations.AddField(
            model_name='issue',
            name='college',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='issues', to='academic.college'),
        ),
        migrations.AddField(
            model_name='issue',
            name='reporter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reported_issues', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='issue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='issues.issue'),
        ),
        migrations.AddField(
            model_name='attachment',
            name='issue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='issues.issue'),
        ),
        migrations.AddField(
            model_name='issuehistory',
            name='issue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history', to='issues.issue'),
        ),
        migrations.AddField(
            model_name='issuehistory',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issue_changes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='notification',
            name='issue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='issues.issue'),
        ),
        migrations.AddField(
            model_name='notification',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='issue',
            name='priority',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='issues', to='issues.priority'),
        ),
        migrations.AddField(
            model_name='issue',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='issues', to='issues.status'),
        ),
    ]
