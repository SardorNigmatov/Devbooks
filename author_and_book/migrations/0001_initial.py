# Generated by Django 4.2.4 on 2023-09-04 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('date_of_birth', models.DateField()),
                ('date_of_death', models.DateField(blank=True, null=True)),
                ('country', models.CharField(default='Uzbekistan', max_length=200)),
                ('genre', models.CharField(max_length=200)),
                ('bio', models.CharField(max_length=1000)),
                ('image', models.ImageField(blank=True, null=True, upload_to='imge/')),
            ],
            options={
                'db_table': 'author',
            },
        ),
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pages', models.IntegerField()),
                ('year', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('genre', models.CharField(max_length=200)),
                ('about_book', models.CharField(max_length=5000)),
                ('image', models.ImageField(blank=True, null=True, upload_to='imge/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='author_and_book.authormodel')),
            ],
            options={
                'db_table': 'books',
            },
        ),
    ]
