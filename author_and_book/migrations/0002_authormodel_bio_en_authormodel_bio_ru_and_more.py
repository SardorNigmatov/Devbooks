# Generated by Django 4.2.4 on 2023-09-04 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author_and_book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authormodel',
            name='bio_en',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='authormodel',
            name='bio_ru',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='authormodel',
            name='bio_uz',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='authormodel',
            name='country_en',
            field=models.CharField(default='Uzbekistan', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='authormodel',
            name='country_ru',
            field=models.CharField(default='Uzbekistan', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='authormodel',
            name='country_uz',
            field=models.CharField(default='Uzbekistan', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='authormodel',
            name='genre_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='authormodel',
            name='genre_ru',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='authormodel',
            name='genre_uz',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='about_book_en',
            field=models.CharField(max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='about_book_ru',
            field=models.CharField(max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='about_book_uz',
            field=models.CharField(max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='title_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='title_ru',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='title_uz',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
