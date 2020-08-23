# Generated by Django 2.1.3 on 2020-08-22 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myform', '0004_auto_20200822_1906'),
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='option_list', to='myform.Question')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='option',
            unique_together={('question', 'text')},
        ),
    ]