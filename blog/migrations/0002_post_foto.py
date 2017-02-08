# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='foto',
            field=models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg'),
        ),
    ]
