# Generated by Django 4.2.1 on 2023-06-21 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0005_dostavka_delete_mymodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dostavka',
            name='location',
            field=models.CharField(choices=[('andijon_tumani', 'Andijon tumani'), ('yangi_bozor', 'Yangi bozor'), ('eski_shahar', 'Eski shahar'), ("o'bekiston_ko'chasi", "O'zbekiston ko'chasi"), ('bobur_kochasi', 'Bobur kochasi'), ("bog'ishamol", "Bog'ishamol"), ('jarqugon', "Jarqo'rg'on")], default=0, max_length=200),
        ),
    ]
