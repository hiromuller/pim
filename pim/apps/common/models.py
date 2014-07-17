# coding=sjis
from django.db import models
from django.contrib import admin

class Team(models.Model):
    """
    �`�[�����f��
    """
    def __unicode__(self):
        return self.name
    # �`�[����
    name = models.CharField(max_length=200)    
    
class Living_situation(models.Model):
    """
    ��炵��
    """
    def __unicode__(self):
        return self.living_situation
    # ��炵��
    living_situation = models.CharField(max_length=200)

class Target(models.Model):
    """
    �^�[�Q�b�g��񃂃f��
    """
    def __unicode__(self):
        return self.name_kanji
    # ���O�i�����j
    name_kanji = models.CharField(max_length=200, blank=True)
    # ���O�i�Ђ炪�ȁj
    name_hiragana = models.CharField(max_length=200, blank=True)
    # ���O�i�p��j
    name_en = models.CharField(max_length=200)
    # ��Փx
    difficulty = models.IntegerField()
    # �ڐG�̖ړI
    purpose = models.CharField(max_length=50)
    # �������
    met_date = models.DateField()
    # ������ꏊ
    met_place = models.CharField(max_length=50)
    # ������V�`���G�[�V����
    met_situation = models.CharField(max_length=200)
    # �a����
    birthday = models.DateField(blank=True)
    # �d�b�ԍ�
    phone_number = models.IntegerField(blank=True)
    # ���[���A�h���X
    mail = models.CharField(max_length=200, blank=True)
    # �Z��
    address = models.CharField(max_length=200, blank=True)
    # �E��
    occupation = models.CharField(max_length=200, blank=True)
    # ���
    company = models.CharField(max_length=200, blank=True)
    # �
    hobby = models.CharField(max_length=200, blank=True)
    # �o�g�n
    birth_place = models.CharField(max_length=200, blank=True)
    # �ЂƂ��炵:1, ����:2, ���[���V�F�A:3 
    living_situation = models.ForeignKey(Living_situation)
    # ���l
    remarks = models.TextField(blank=True)
    # ���i1
    type_1 = models.CharField(max_length=200)
    # ���i2
    type_2 = models.CharField(max_length=200)
    # ���i3
    type_3 = models.CharField(max_length=200)
    # �I���t���O
    done_flg = models.BooleanField(default=False)

class User (models.Model):
    """
    ���[�U���f��
    """
    def __unicode__(self):
        return self.name_kanji
    # ���[�UID
    user_id = models.CharField(max_length=6, primary_key=True)
    # ���O�i�����j
    name_kanji = models.CharField(max_length=200, blank=True)
    # ���O�i�Ђ炪�ȁj
    name_hiragana = models.CharField(max_length=200, blank=True)
    # ���O�i�p��j
    name_en = models.CharField(max_length=200)
    # �p�X���[�h
    password = models.CharField(max_length=10)
    # �`�[��
    team = models.ForeignKey(Team)
    # �o�g�n
    birthday = models.DateField(blank=True)
    # �Ώې��i1
    target_type_1 = models.CharField(max_length=200)
    # �Ώې��i2
    target_type_2 = models.CharField(max_length=200)
    # �Ώې��i3
    target_type_3 = models.CharField(max_length=200)
    
class Responsible(models.Model):
    """
    �S���Ғ�`���f��
    """
    def __unicode__(self):
        return self.responsible_by
    # �ڋq
    target = models.ForeignKey(Target)
    # �S����
    responsible_by = models.ForeignKey(User)
    # �֌W���B�F�l:1,�������:2,��i:3,��Г���:4,��Ќ�y:5,��w����:6,��w��y:7,��w��y:8,�n��:9,��������:10,���l:11,�قڒm��Ȃ�:12
    relationship = models.IntegerField()
    #�i����
    progress_status = models.TextField(blank=True)
    
admin.site.register(Target)
admin.site.register(Living_situation)
admin.site.register(User)
admin.site.register(Team)
admin.site.register(Responsible)
