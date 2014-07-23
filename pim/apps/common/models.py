# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin

    
class Living_situation(models.Model):
    """
    ��炵��
    """
    def __unicode__(self):
        return self.living_situation
    # ��炵��
    living_situation = models.CharField(max_length=200)

class Type(models.Model):
    """
    ���i
    """
    def __unicode__(self):
        return self.type
    # ���i
    type = models.CharField(max_length=200)
    
class Level(models.Model):
    """
    ���i
    """
    def __unicode__(self):
        return self.level_description
    # ���x������
    level_description = models.CharField(max_length=50)

class Target(models.Model):
    """
    �^�[�Q�b�g��񃂃f��
    """
    def __unicode__(self):
        return self.name_kanji
    # ���O�i�����j
    name_kanji = models.CharField(max_length=200)
    # ���O�i�Ђ炪�ȁj
    name_hiragana = models.CharField(max_length=200, blank=True)
    # ���O�i�p��j
    name_en = models.CharField(max_length=200)
    # ��Փx
    difficulty = models.IntegerField(blank=True, null=True)
    #���x��
    level = models.ForeignKey(Level, null=True)
    # �ڐG�̖ړI
    purpose = models.CharField(max_length=50, blank=True)
    # �������
    met_date = models.DateField()
    # ������ꏊ
    met_place = models.CharField(max_length=50, blank=True)
    # ������V�`���G�[�V����
    met_situation = models.CharField(max_length=200, blank=True)
    # �a����
    birthday = models.DateField(blank=True, null=True)
    # �d�b�ԍ�
    phone_number = models.IntegerField(blank=True, null=True)
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
    living_situation = models.ForeignKey(Living_situation, blank=True, null=True)
    # ���l
    remarks = models.TextField(blank=True)
    # ���i1
    type_1 = models.ForeignKey(Type, related_name='type_1', blank=True, null=True)
    # ���i2
    type_2 = models.ForeignKey(Type, related_name='type_2', blank=True, null=True)
    # ���i3
    type_3 = models.ForeignKey(Type, related_name='type_3', blank=True, null=True)
    # �I���t���O
    done_flg = models.BooleanField(default=False)

class Introduce(models.Model):
    """
    �Љ�ҊǗ�
    """
    def __unicode__(self):
        return self.introduced_by
    #�Љ�ꂽ�l
    target = models.ForeignKey(Target, related_name='target')
    #�Љ��
    introduced_by = models.ForeignKey(Target, related_name='introduced_by')

class Target_relationship(models.Model):
    """
    �^�[�Q�b�g���m�̊֌W��
    """
    def __unicode__(self):
        return self.relationship
    #�^�[�Q�b�g1
    target1 = models.ForeignKey(Target, related_name='target1')
    #�^�[�Q�b�g2
    target2 = models.ForeignKey(Target, related_name='target2')
    #�֌W��
    relationship = models.CharField(max_length=200)
    
class Team(models.Model):
    """
    �`�[�����f��
    """
    def __unicode__(self):
        return self.name
    # �`�[����
    name = models.CharField(max_length=200)    

class User (models.Model):
    """
    ���[�U���f��
    """
    def __unicode__(self):
        return self.name_kanji
    # ���[�UID
    login_id = models.CharField(max_length=20, primary_key=True)
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
    birthday = models.DateField(blank=True, null=True)
    #�o�g�n
    birth_place = models.CharField(max_length=200, blank=True)
    # �Ώې��i1
    target_type_1 = models.ForeignKey(Type, related_name='target_type_1', blank=True, null=True)
    # �Ώې��i2
    target_type_2 = models.ForeignKey(Type, related_name='target_type_2', blank=True, null=True)
    # �Ώې��i3
    target_type_3 = models.ForeignKey(Type, related_name='target_type_3', blank=True, null=True)

    
class Progress(models.Model):
    """
    �i���}�X�^
    """
    def __unicode__(self):
        return self.progress_name
    #�i����
    progress_name = models.CharField(max_length=50)
    
class Progress_management(models.Model):
    """
    �S���Ғ�`���f��
    """
    def __unicode__(self):
        return unicode(self.progress)
    # �ڋq
    target = models.ForeignKey(Target)
    # �S����
    responsible_by = models.ForeignKey(User)
    # �֌W���B�F�l:1,����:2,��i:3,��Г���:4,��Ќ�y:5,��w����:6,��w��y:7,��w��y:8,�n��:9,��������:10,���l:11,�قڒm��Ȃ�:12
    relationship = models.CharField(max_length=200)
    #�i����
    progress = models.ForeignKey(Progress)
    #���l
    remarks = models.CharField(max_length=200, blank=True)

admin.site.register(Living_situation)
admin.site.register(Type)
admin.site.register(Level)
admin.site.register(Target)
admin.site.register(Introduce)
admin.site.register(Target_relationship)
admin.site.register(Team)
admin.site.register(User)
admin.site.register(Progress)
admin.site.register(Progress_management)
