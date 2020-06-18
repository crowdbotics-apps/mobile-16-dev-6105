# Generated by Django 2.2.13 on 2020-06-18 08:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0005_auto_20200618_0824'),
    ]

    operations = [
        migrations.CreateModel(
            name='JHjhjh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bvcnbcnvb', models.BigIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='customtext',
            name='ftghryuj5y',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customtext_ftghryuj5y', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='customtext',
            name='sfasdfasz',
            field=models.ManyToManyField(blank=True, related_name='customtext_sfasdfasz', to='home.HomePage'),
        ),
        migrations.AddField(
            model_name='ghvhggfgvcafvwse',
            name='sdfaef',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ghvhggfgvcafvwse_sdfaef', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='homepage',
            name='werqwrf',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='homepage_werqwrf', to=settings.AUTH_USER_MODEL),
        ),
    ]
