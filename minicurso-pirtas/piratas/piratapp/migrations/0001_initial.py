# Generated by Django 2.0 on 2018-04-20 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tesouro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
                ('quantidade', models.IntegerField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('img_tesouro', models.ImageField(upload_to='imgs')),
            ],
        ),
    ]
