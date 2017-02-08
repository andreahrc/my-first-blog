# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_foto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='foto',
            new_name='foto_1',
        ),
        migrations.AddField(
            model_name='post',
            name='foto_2',
            field=models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg'),
        ),
        migrations.AddField(
            model_name='post',
            name='foto_3',
            field=models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg'),
        ),
    ]
