# Generated by Django 4.1.2 on 2022-12-02 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_signupuser_signup_master_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='signup_master',
            new_name='signupuser',
        ),
    ]