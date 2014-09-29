# -*- coding: utf-8 -*-
'''
Created on 2014/08/13

@author: ex_hrs
'''

"""
CHOICES
"""
"""
living situation
"""
LIVING_SITUATION_CHOICES = (
                            ('LONE',u'一人暮らし'),
                            ('FAMILY',u'実家'),
                            ('DORMITORY',u'寮'),
                            ('SHARE',u'シェアハウス'),
                            ('ETC',u'その他')
                            )
"""
type
"""
TYPE_CHOICES = (
                ('OUTGOING',u'元気'),
                ('DRINKER',u'酒好き'),
                ('LEADER',u'幹事'),
                ('STUDIOUS',u'真面目')
                )
"""
level
"""
LEVEL_CHOICES = (
                 (1,u'1:辛うじて人の形を保っている。クリーチャーレベル。煮ても焼いても食えません。'),
                 (2,u'2:正気を失えば食べられる'),
                 (3,u'3:普通よりチョイ劣る'),
                 (4,u'4:普通'),
                 (5,u'5:普通よりチョイかわいい。(個人の好みがかなり出る)'),
                 (6,u'6:かわいい'),
                 (7,u'7:かなりかわいい(すれ違ったら振り返る)'),
                 (8,u'8:モデル・芸能人・アイドルと同格。ここいらになるとKで遭遇するのはまずありえません。奇跡。'),
                 (9,u'9:モデル・芸能人・アイドルそのもの'),
                 (10,u'10:神'),
                 )
"""
progress
"""
PROGRESS_CHOICES = (
                    ('NEW',u'新規'),
                    ('TOUCH',u'着手'),
                    ('IN_PROGRESS',u'進行中'),
                    ('COMPLETED',u'完了'),
                    ('FINISHED',u'終了')
                    )
"""
difficulty
"""
DIFFICULTY_CHOICES = (
                      ('EASY', u'易しい'),
                      ('NOMRAL', u'普通'),
                      ('HARD', u'難しい')
                      )

"""
定数
"""
RESPONSIBLE_TARGET_LIST_NAME = u'担当ターゲット'
REGISTERED_TARGET_LIST_NAME = u'登録したターゲット'
TEAM_TARGET_LIST_NAME = u'チームターゲット'

MAX_NUM_LATEST_PROGRESS_LIST = 50