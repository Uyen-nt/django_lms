# Generated by Django 5.1.1 on 2024-09-06 09:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question_bank', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='correct_answer',
        ),
        migrations.RemoveField(
            model_name='question',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='question',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='answer',
            name='text',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.ForeignKey(default=0.0005263157894736842, on_delete=django.db.models.deletion.CASCADE, to='question_bank.category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question_bank.subject'),
        ),
    ]