# Generated by Django 3.2.9 on 2022-07-14 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_name', models.CharField(max_length=69, unique=True)),
                ('VoterID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('DOB', models.DateField(blank=True, default=None, null=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cn_Registeration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Candidate_Name', models.CharField(max_length=69, unique=True)),
                ('Party', models.CharField(max_length=60, unique=True)),
                ('Mobile', models.CharField(max_length=13, unique=True)),
                ('Gender', models.CharField(max_length=60)),
                ('doc_file', models.FileField(blank=True, null=True, upload_to='documents/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BJP', models.CharField(blank=True, max_length=13, null=True)),
                ('INC', models.CharField(blank=True, max_length=13, null=True)),
                ('BSP', models.CharField(blank=True, max_length=13, null=True)),
                ('TMC', models.CharField(blank=True, max_length=13, null=True)),
                ('NCP', models.CharField(blank=True, max_length=13, null=True)),
                ('NPP', models.CharField(blank=True, max_length=13, null=True)),
                ('AAP', models.CharField(blank=True, max_length=13, null=True)),
                ('JDU', models.CharField(blank=True, max_length=13, null=True)),
                ('RJD', models.CharField(blank=True, max_length=13, null=True)),
                ('SP', models.CharField(blank=True, max_length=13, null=True)),
                ('CPI', models.CharField(blank=True, max_length=13, null=True)),
                ('CPIM', models.CharField(blank=True, max_length=13, null=True)),
                ('RLD', models.CharField(blank=True, max_length=13, null=True)),
                ('NOTA', models.CharField(blank=True, max_length=13, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Registeration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=69)),
                ('Email', models.EmailField(max_length=254)),
                ('Mobile', models.CharField(max_length=13)),
                ('Address', models.CharField(max_length=100)),
                ('Aadhar', models.CharField(max_length=12, unique=True)),
                ('VoterID', models.CharField(max_length=10, unique=True)),
                ('DOB', models.DateField(default='2022/07/14')),
            ],
        ),
    ]
