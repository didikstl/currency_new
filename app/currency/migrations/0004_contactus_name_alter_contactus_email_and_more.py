# Generated by Django 4.2.7 on 2023-12-09 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0003_alter_contactus_email_alter_source_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='name',
            field=models.CharField(default='admin', max_length=64, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='email',
            field=models.EmailField(default='bond007@gmail.com', max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='message',
            field=models.TextField(max_length=254, verbose_name='Message'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='subject',
            field=models.TextField(max_length=254, verbose_name='Subject'),
        ),
    ]
