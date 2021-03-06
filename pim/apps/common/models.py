# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
import consts as CONST


#class Living_situation(models.Model):
#    """
#    暮らし状況
#    """
#    def __unicode__(self):
#        return self.living_situation
    # 暮らし状況
#    living_situation = models.CharField(max_length=200)

#    def encode(self):
#        return {
#                'living_situation': self.living_situation,
#                }

#class Type(models.Model):
#    """
#    性格
#    """
#    def __unicode__(self):
#        return self.type
#    # 性格
#    type = models.CharField(max_length=200)

#    def encode(self):
#        return {
#                'type': self.type,
#                }

#class Level(models.Model):
#    """
#    レベル
#    """
#    def __unicode__(self):
#        return self.level_description
#    # レベル説明
#    level_description = models.CharField(max_length=50)

#    def encode(self):
#        return {
#                'level_description': self.level_description,
#                }

class Target(models.Model):
    """
    ターゲット情報モデル
    """
    def __unicode__(self):
        return self.name
    # 名前（漢字）
    name = models.CharField(max_length=200)
    # よみかた）
    reading = models.CharField(max_length=200)
    # 呼び名
    nick_name = models.CharField(max_length=200, blank=True)
    # 難易度
    difficulty = models.CharField(max_length=200, blank=True, null=True, choices=CONST.DIFFICULTY_CHOICES)
    #レベル
    level = models.IntegerField(choices=CONST.LEVEL_CHOICES)
    # 接触の目的
    purpose = models.CharField(max_length=50)
    # 会った日
    met_date = models.DateField()
    # 会った場所
    met_place = models.CharField(max_length=50, blank=True)
    # 会ったシチュエーション
    met_situation = models.CharField(max_length=200, blank=True)
    # 誕生日
    birthday = models.DateField(blank=True, null=True)
    # 電話番号
    phone_number = models.CharField(max_length=11, blank=True, null=True)
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
    living_situation = models.CharField(max_length=200, blank=True, null=True, choices=CONST.LIVING_SITUATION_CHOICES)
    # 備考
    remarks = models.TextField(blank=True)
    # 性格1
    type_1 = models.CharField(max_length=200, blank=True, null=True, choices=CONST.TYPE_CHOICES)
    # 性格2
    type_2 = models.CharField(max_length=200, blank=True, null=True, choices=CONST.TYPE_CHOICES)
    # 性格3
    type_3 = models.CharField(max_length=200, blank=True, null=True, choices=CONST.TYPE_CHOICES)
    # 担当者ありフラグ
    taken_flg = models.BooleanField(default=False)
    # 終了フラグ
    done_flg = models.BooleanField(default=False)
    # ターゲット画像
    target_photo = models.ImageField(upload_to='targetPhoto/', null=True, blank=True)

    def encode(self):
        return {
                'name': self.name,
                'reading': self.reading,
                'difficulty': self.difficulty,
                'level': self.level,
                'purpose': self.purpose,
                'met_date': self.met_date,
                'met_place': self.met_place,
                'met_situation': self.met_situation,
                'birthday': self.birthday,
                'phone_number': self.phone_number,
                'mail': self.mail,
                'address': self.address,
                'occupation': self.occupation,
                'company': self.company,
                'hobby': self.hobby,
                'birth_place': self.birth_place,
                'living_situation': self.living_situation,
                'remarks': self.remarks,
                'type_1': self.type_1,
                'type_2': self.type_2,
                'type_3': self.type_3,
                'done_flg': self.done_flg,
                }

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

    def encode(self):
        return {
                'target': self.target.encode(),
                'introduced_by': self.introduced_by.encode(),
                }

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

    def encode(self):
        return {
                'target1': self.target1.encode(),
                'target2': self.target2.encode(),
                'relationship': self.relationship,
                }

class Team(models.Model):
    """
    チームモデル
    """
    def __unicode__(self):
        return self.name
    # チーム名
    name = models.CharField(max_length=200)
    # メンバー上限
    team_size = models.IntegerField(default=5)

    def encode(self):
        return {
                'name': self.name,
                }

class CustomUserManager(models.Manager):
    def create_user(self, username, email):
        return self.model._default_manager.create(username=username)

class User (models.Model):
    """
    ユーザモデル
    """
    def __unicode__(self):
        return self.username
    # ユーザID
    username = models.CharField(max_length=20, primary_key=True)
    # 名前（漢字）
    name = models.CharField(max_length=200, blank=True, verbose_name='名前(漢字)')
    # 名前（ひらがな）
    name_hiragana = models.CharField(max_length=200, blank=True, verbose_name='名前(ひらがな)')
    # 名前（英語）
    name_en = models.CharField(max_length=200, blank=True, verbose_name='名前(英語)')
    # チーム
    team = models.ForeignKey(Team, blank=True, null=True, verbose_name='チーム')
    # 誕生日
    birthday = models.DateField(blank=True, null=True, verbose_name='誕生日')
    # 出身地
    birth_place = models.CharField(max_length=200, blank=True, verbose_name='出身地')
    # 対象性格1
    target_type_1 = models.CharField(max_length=200, blank=True, null=True, choices=CONST.TYPE_CHOICES, verbose_name='対象性格1')
    # 対象性格2
    target_type_2 = models.CharField(max_length=200, blank=True, null=True, choices=CONST.TYPE_CHOICES, verbose_name='対象性格2')
    # 対象性格3
    target_type_3 = models.CharField(max_length=200, blank=True, null=True, choices=CONST.TYPE_CHOICES, verbose_name='対象性格3')
    # email
    email = models.CharField(max_length=200, verbose_name='Email')
    # プロファイル画像
    profile_photo = models.URLField(max_length=200, blank=True)
    # is_active
    is_active  = models.BooleanField(default=True)
    # last login
    last_login = models.DateTimeField(blank=True, null=True)
    #チーム管理者フラグ
#    team_admin_flg = models.BooleanField(default=False)
    # ユーザの状態。0=アカウント停止、1=仮登録、2=無料会員、3=有料会員
    status = models.IntegerField(default=1)

    objects = CustomUserManager();

    def is_authenticated(self):
        return True

    def encode(self):
        return {
                'username': self.username,
                'name': self.name,
                'name_hiragana': self.name_hiragana,
                'name_en': self.name_en,
                'team': self.team,
                'birthday': self.birthday,
                'birth_place': self.birth_place,
                'target_type_1': self.target_type_1,
                'target_type_2': self.target_type_2,
                'target_type_3': self.target_type_3,
                'profile_photo': self.profile_photo,
                }

class Membership(models.Model):
    """
    チームとメンバーの関係の中間モデル
    """
    def __unicode__(self):
        return self.team.name

    # チーム
    team = models.ForeignKey(Team)
    # ユーザ
    user = models.ForeignKey(User)
    # チーム管理者フラグ
    team_admin_flg = models.BooleanField(default=False)

    def encode(self):
        return {
                'team': self.team.encode(),
                'user': self.ruser.encode(),
                'team_admin_flg': self.team_admin_flg.encode(),
                }


class Invitation(models.Model):
    """
    チーム招待中間モデル
    """
    def __unicode__(self):
        return self.team

    # チーム
    team = models.ForeignKey(Team)
    # 被招待者
    invited_user = models.ForeignKey(User, related_name="invited_user")
    # 招待者
    invited_by = models.ForeignKey(User, related_name="invited_by")
    # 管理者承認フラグ
    approve_by_admin_flg = models.BooleanField(default=False)
    # 被招待者承認フラグ
    approve_by_user_flg = models.BooleanField(default=False)

#class Progress(models.Model):
#    """
#    進捗マスタ
#    """
#    def __unicode__(self):
#        return self.progress_name
#    #進捗名
#    progress_name = models.CharField(max_length=50)

#    def encode(self):
#        return {
#                'progress_name': self.progress_name,
#                }

class Progress_management(models.Model):
    """
    担当者定義モデル
    """
    def __unicode__(self):
        return unicode(self.progress)
    # 顧客
    target = models.ForeignKey(Target, verbose_name='顧客')
    # 担当者
    responsible_by = models.ForeignKey(User, verbose_name='担当者')
    # 関係性
    relationship = models.CharField(max_length=200, verbose_name='関係性')
    # 進捗状況
    progress = models.CharField(max_length=200, choices=CONST.PROGRESS_CHOICES, verbose_name='進捗状況')
    # 備考
    remarks = models.TextField(blank=True, verbose_name='備考')
    # 登録日時
    registered_at = models.DateTimeField(auto_now_add=True, verbose_name='登録日時')

    def encode(self):
        return {
                'target': self.target.encode(),
                'responsible_by': self.responsible_by.encode(),
                'relationship': self.relationship,
                'progress': self.progress,
                'remarks': self.remarks,
                }

class Target_register(models.Model):
    """
    ターゲット登録者モデル
    """
    def __unicode__(self):
        return unicode(self.pk)
    # ターゲット
    target = target = models.ForeignKey(Target, verbose_name='顧客')
    # ユーザ
    user = models.ForeignKey(User)

class Statement(models.Model):
    """
    承諾書モデル
    """
    def __unicode__(self):
        return unicode(self.pk)
    #種別 とりあえず１
    type = models.IntegerField(default = 1)
    #タイトル
    title = models.CharField(max_length=200)
    #本文
    statement = models.CharField(max_length=1000)

class Statement_Agreement(models.Model):
    """
    個人情報取り扱い注意同意テーブル
    """
    def __unicode__(self):
        return unicode(self.pk)
    #ユーザ
    user = models.ForeignKey(User)
    #同意
    agreement = models.BooleanField(default=False)
    #同意した時間
    agreement_time = models.DateTimeField(auto_now_add=True)
    #本文
    statement = models.ForeignKey(Statement)


#admin.site.register(Living_situation)
#admin.site.register(Type)
#admin.site.register(Level)
admin.site.register(Target)
admin.site.register(Introduce)
admin.site.register(Target_relationship)
admin.site.register(Team)
admin.site.register(User)
admin.site.register(Membership)
admin.site.register(Invitation)
#admin.site.register(Progress)
admin.site.register(Progress_management)
admin.site.register(Target_register)
admin.site.register(Statement)
admin.site.register(Statement_Agreement)