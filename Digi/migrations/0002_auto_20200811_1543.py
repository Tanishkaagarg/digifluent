
# Generated by Django 3.0.8 on 2020-08-11 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Digi', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='content',
            new_name='brandingservice',
        ),
        migrations.RenameModel(
            old_name='contact',
            new_name='contactservice',
        ),
        migrations.RenameModel(
            old_name='email',
            new_name='contentservice',
        ),
        migrations.RenameModel(
            old_name='webdesigning',
            new_name='creativeservice',
        ),
        migrations.RenameModel(
            old_name='graphic',
            new_name='emailservice',
        ),
        migrations.RenameModel(
            old_name='sem',
            new_name='facebookservice',
        ),
        migrations.RenameModel(
            old_name='influencer',
            new_name='googleservice',
        ),
        migrations.RenameModel(
            old_name='facebook',
            new_name='graphicservice',
        ),
        migrations.RenameModel(
            old_name='branding',
            new_name='influencerservice',
        ),
        migrations.RenameModel(
            old_name='creative',
            new_name='semservice',
        ),
        migrations.RenameModel(
            old_name='seo',
            new_name='seoservice',
        ),
        migrations.RenameModel(
            old_name='google',
            new_name='socialmediamarketingservice',
        ),
        migrations.RenameModel(
            old_name='socialmediamarketing',
            new_name='webdesigningservice',
        ),
    ]