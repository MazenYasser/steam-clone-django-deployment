# Generated by Django 3.2.7 on 2023-08-18 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0008_games_img_1_games_img_2_games_img_3_games_img_cover_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='img_logo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%y/%m/%d', verbose_name='Logo Image'),
        ),
    ]
