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
    # �`�[��
    team = models.ForeignKey(Team)
    # �E��
    occupation = models.CharField(max_length=200, blank=True)
    # ���
    company = models.CharField(max_length=200, blank=True)
    # �
    hobby = models.CharField(max_length=200, blank=True)
    # �o�g�n
    birth_place = models.CharField(max_length=200, blank=True)
    # �ЂƂ��炵:1, ����:2, ���[���V�F�A:3 
    living_situation = models.IntegerField(null=True)
    # ���l
    remarks = models.TextField(blank=True)
    # ���i1
    character_1 = models.IntegerField(null=True)
    # ���i2
    character_2 = models.IntegerField(null=True)
    # ���i3
    character_3 = models.IntegerField(null=True)
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
    birth_place = models.CharField(max_length=200)
    # �Ώې��i1
    target_character_1 = models.IntegerField(blank=True)
    # �Ώې��i2
    target_character_2 = models.IntegerField(blank=True)
    # �Ώې��i3
    target_character_3 = models.IntegerField(blank=True)
    
class Responsible(models.Model):
    """
    �S���Ғ�`���f��
    """
    def __unicode__(self):
        return self.responsible_by
    # �ڋq
    customer = models.ForeignKey(Target)
    # �S����
    responsible_by = models.ForeignKey(User)
    # �֌W���B�F�l:1,�������:2,��i:3,��Г���:4,��Ќ�y:5,��w����:6,��w��y:7,��w��y:8,�n��:9,��������:10,���l:11,�قڒm��Ȃ�:12
    relationship = models.IntegerField()
    
admin.site.register(Target)
admin.site.register(User)
admin.site.register(Team)
admin.site.register(Responsible)
