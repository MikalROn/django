# Generated by Django 4.1.7 on 2023-03-14 00:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('omieemprestimos', '0003_remove_lojas_apikey_remove_lojas_apisecret'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emprestimos',
            name='credor',
        ),
        migrations.RemoveField(
            model_name='emprestimos',
            name='devedor',
        ),
        migrations.AlterField(
            model_name='emprestimos',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AddField(
            model_name='emprestimos',
            name='credor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='emprestimos_credor', to='omieemprestimos.lojas'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='emprestimos',
            name='devedor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='emprestimos_devedor', to='omieemprestimos.lojas'),
            preserve_default=False,
        ),
    ]
