# Generated by Django 3.2.5 on 2021-07-27 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment_app', '0003_alter_replycomment_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='image',
            field=models.ImageField(default='author-3.jpg', upload_to='comment'),
        ),
    ]
