# Generated by Django 4.2.15 on 2024-08-21 16:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mini_quiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerAnswers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_correct', models.BooleanField()),
                ('time_answered', models.DateTimeField()),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mini_quiz.question')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
