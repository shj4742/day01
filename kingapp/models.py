from django.db import models

# Create your models here.
class GrowUp(models.Model):
    wugong = models.IntegerField('物理攻击', db_column='wogong')
    fagong = models.IntegerField('法术攻击', db_column='fagong')
    shengming = models.IntegerField('生命', db_column='shengming')
    fali = models.IntegerField('法力', db_column='fali')



class HeroInfo(models.Model):
    hname = models.CharField('英雄名', max_length=20, db_column='hname')
    hgender = models.BooleanField('性别',db_column='hgender')
    hprofession = models.CharField('职业',max_length=20, db_column='hprofession')
    hlaunch_date = models.DateTimeField('发布时间', auto_now_add=True)

    def __str__(self):
        return self.hname


class SkinInfo(models.Model):
    sname = models.CharField('皮肤名', max_length=20, db_column='sname')
    scontent = models.CharField('简介', max_length=1000, db_column='scontent')
    image = models.ImageField('图片', upload_to = 'heroSkin')
    shero = models.ForeignKey(HeroInfo)
    def __str__(self):
        return self.sname