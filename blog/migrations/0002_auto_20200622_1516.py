# Generated by Django 3.0.7 on 2020-06-22 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='Post',  # モデル名
            old_name='autor',  # 変更前
            new_name='author'  # 変更後
        )
    ]
