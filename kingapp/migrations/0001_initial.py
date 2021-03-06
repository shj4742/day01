# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-11-03 06:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GrowUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wugong', models.IntegerField(db_column='wogong', verbose_name='物理攻击')),
                ('fagong', models.IntegerField(db_column='fagong', verbose_name='法术攻击')),
                ('shengming', models.IntegerField(db_column='shengming', verbose_name='生命')),
                ('fali', models.IntegerField(db_column='fali', verbose_name='法力')),
            ],
        ),
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hname', models.CharField(db_column='hname', max_length=20, verbose_name='英雄名')),
                ('hgender', models.BooleanField(db_column='hgender', verbose_name='性别')),
                ('hprofession', models.CharField(db_column='hprofession', max_length=20, verbose_name='职业')),
                ('hlaunch_date', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
            ],
        ),
        migrations.CreateModel(
            name='SkinInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(db_column='sname', max_length=20, verbose_name='皮肤名')),
                ('scontent', models.CharField(db_column='scontent', max_length=1000, verbose_name='简介')),
                ('image', models.ImageField(upload_to='', verbose_name='图片')),
                ('shero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kingapp.HeroInfo')),
            ],
        ),
    ]
