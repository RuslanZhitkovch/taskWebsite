# Generated by Django 4.1.3 on 2022-11-10 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('task', models.TextField(null=True, verbose_name='Описание')),
                ('published', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Время публикации')),
            ],
        ),
    ]