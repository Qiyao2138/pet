# Generated by Django 3.1.7 on 2021-04-01 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of pet', max_length=100)),
                ('breed', models.CharField(help_text='Breed of pet', max_length=100)),
                ('sex', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], default='other', help_text='Sex of pet', max_length=15)),
                ('birth_date', models.DateField(help_text='Birth date of pet')),
                ('vaccinated', models.BooleanField(help_text='Whether or not pet is vaccinated')),
                ('profile_image', models.ImageField(blank=True, help_text='Profile picture of pet', upload_to='profiles_images')),
                ('bio', models.TextField(blank=True)),
            ],
        ),
    ]
