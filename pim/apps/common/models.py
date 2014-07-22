# coding=sjis
from django.db import models
from django.contrib import admin

    
class Living_situation(models.Model):
    """
    暮らし状況
    """
    def __unicode__(self):
        return self.living_situation
    # 暮らし状況
    living_situation = models.CharField(max_length=200)

class Type(models.Model):
    """
    性格
    """
    def __unicode__(self):
        return self.type
    # 性格
    type = models.CharField(max_length=200)
    
class Level(models.Model):
    """
    性格
    """
    def __unicode__(self):
        return self.level_description
    # レベル説明
    level_description = models.CharField(max_length=50)

class Target(models.Model):
    """
    ターゲット情報モデル
    """
    def __unicode__(self):
        return self.name_kanji
    # 名前（漢字）
    name_kanji = models.CharField(max_length=200, blank=True)
    # 名前（ひらがな）
    name_hiragana = models.CharField(max_length=200, blank=True)
    # 名前（英語）
    name_en = models.CharField(max_length=200)
    # 難易度
    difficulty = models.IntegerField(blank=True, null=True)
    #レベル
    level = models.ForeignKey(Level, null=True)
    # 接触の目的
    purpose = models.CharField(max_length=50, blank=True)
    # 会った日
    met_date = models.DateField()
    # 会った場所
    met_place = models.CharField(max_length=50, blank=True)
    # 会ったシチュエーション
    met_situation = models.CharField(max_length=200, blank=True)
    # 誕生日
    birthday = models.DateField(blank=True, null=True)
    # 電話番号
    phone_number = models.IntegerField(blank=True, null=True)
    # メールアドレス
    mail = models.CharField(max_length=200, blank=True)
    # 住所
    address = models.CharField(max_length=200, blank=True)
    # 職業
    occupation = models.CharField(max_length=200, blank=True)
    # 会社
    company = models.CharField(max_length=200, blank=True)
    # 趣味
    hobby = models.CharField(max_length=200, blank=True)
    # 出身地
    birth_place = models.CharField(max_length=200, blank=True)
    # ひとり暮らし:1, 実家:2, ルームシェア:3 
    living_situation = models.ForeignKey(Living_situation, blank=True, null=True)
    # 備考
    remarks = models.TextField(blank=True)
    # 性格1
    type_1 = models.ForeignKey(Type, related_name='type_1', blank=True, null=True)
    # 性格2
    type_2 = models.ForeignKey(Type, related_name='type_2', blank=True, null=True)
    # 性格3
    type_3 = models.ForeignKey(Type, related_name='type_3', blank=True, null=True)
    # 終了フラグ
    done_flg = models.BooleanField(default=False)

class Introduce(models.Model):
    """
    紹介者管理
    """
    def __unicode__(self):
        return self.introduced_by
    #紹介された人
    target = models.ForeignKey(Target, related_name='target')
    #紹介者
    introduced_by = models.ForeignKey(Target, related_name='introduced_by')

class Target_relationship(models.Model):
    """
    ターゲット同士の関係性
    """
    def __unicode__(self):
        return self.relationship
    #ターゲット1
    target1 = models.ForeignKey(Target, related_name='target1')
    #ターゲット2
    target2 = models.ForeignKey(Target, related_name='target2')
    #関係性
    relationship = models.CharField(max_length=200)
    
class Team(models.Model):
    """
    チームモデル
    """
    def __unicode__(self):
        return self.name
    # チーム名
    name = models.CharField(max_length=200)    

class User (models.Model):
    """
    ユーザモデル
    """
    def __unicode__(self):
        return self.name_kanji
    # ユーザID
    login_id = models.CharField(max_length=20, primary_key=True)
    # 名前（漢字）
    name_kanji = models.CharField(max_length=200, blank=True)
    # 名前（ひらがな）
    name_hiragana = models.CharField(max_length=200, blank=True)
    # 名前（英語）
    name_en = models.CharField(max_length=200)
    # パスワード
    password = models.CharField(max_length=10)
    # チーム
    team = models.ForeignKey(Team)
    # 出身地
    birthday = models.DateField(blank=True, null=True)
    #出身地
    birth_place = models.CharField(max_length=200, blank=True)
    # 対象性格1
    target_type_1 = models.ForeignKey(Type, related_name='target_type_1', blank=True, null=True)
    # 対象性格2
    target_type_2 = models.ForeignKey(Type, related_name='target_type_2', blank=True, null=True)
    # 対象性格3
    target_type_3 = models.ForeignKey(Type, related_name='target_type_3', blank=True, null=True)

    
class Progress(models.Model):
    """
    進捗マスタ
    """
    def __unicode__(self):
        return self.progress_name
    #進捗名
    progress_name = models.CharField(max_length=50)
    
class Progress_management(models.Model):
    """
    担当者定義モデル
    """
    def __unicode__(self):
        return self.progress
    # 顧客
    target = models.ForeignKey(Target)
    # 担当者
    responsible_by = models.ForeignKey(User)
    # 関係性。友人:1,取引相手:2,上司:3,会社同期:4,会社後輩:5,大学同期:6,大学先輩:7,大学後輩:8,地元:9,幹事仲間:10,恋人:11,ほぼ知らない:12
    relationship = models.CharField(max_length=200)
    #進捗状況
    progress = models.ForeignKey(Progress)
    #備考
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
