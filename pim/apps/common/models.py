# coding=sjis
from django.db import models
from django.contrib import admin

class Team(models.Model):
    """
    チームモデル
    """
    def __unicode__(self):
        return self.name
    # チーム名
    name = models.CharField(max_length=200)    
    
class Living_situation(models.Model):
    """
    暮らし状況
    """
    def __unicode__(self):
        return self.living_situation
    # 暮らし状況
    living_situation = models.CharField(max_length=200)

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
    difficulty = models.IntegerField()
    # 接触の目的
    purpose = models.CharField(max_length=50)
    # 会った日
    met_date = models.DateField()
    # 会った場所
    met_place = models.CharField(max_length=50)
    # 会ったシチュエーション
    met_situation = models.CharField(max_length=200)
    # 誕生日
    birthday = models.DateField(blank=True)
    # 電話番号
    phone_number = models.IntegerField(blank=True)
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
    living_situation = models.ForeignKey(Living_situation)
    # 備考
    remarks = models.TextField(blank=True)
    # 性格1
    type_1 = models.CharField(max_length=200)
    # 性格2
    type_2 = models.CharField(max_length=200)
    # 性格3
    type_3 = models.CharField(max_length=200)
    # 終了フラグ
    done_flg = models.BooleanField(default=False)

class User (models.Model):
    """
    ユーザモデル
    """
    def __unicode__(self):
        return self.name_kanji
    # ユーザID
    user_id = models.CharField(max_length=6, primary_key=True)
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
    birthday = models.DateField(blank=True)
    # 対象性格1
    target_type_1 = models.CharField(max_length=200)
    # 対象性格2
    target_type_2 = models.CharField(max_length=200)
    # 対象性格3
    target_type_3 = models.CharField(max_length=200)
    
class Responsible(models.Model):
    """
    担当者定義モデル
    """
    def __unicode__(self):
        return self.responsible_by
    # 顧客
    target = models.ForeignKey(Target)
    # 担当者
    responsible_by = models.ForeignKey(User)
    # 関係性。友人:1,取引相手:2,上司:3,会社同期:4,会社後輩:5,大学同期:6,大学先輩:7,大学後輩:8,地元:9,幹事仲間:10,恋人:11,ほぼ知らない:12
    relationship = models.IntegerField()
    #進捗状況
    progress_status = models.TextField(blank=True)
    
admin.site.register(Target)
admin.site.register(Living_situation)
admin.site.register(User)
admin.site.register(Team)
admin.site.register(Responsible)
