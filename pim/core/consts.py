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
                ('LEADER',u'幹事')
                ('STUDIOUS',u'真面目')
                )
"""
level
"""
LEVEL_CHOICES = (
                 (1,u'1:よろしくない'),
                 (2,u'2:グループなら飲みに行ける'),
                 (3,u'3:ギリギリサシ飲み'),
                 (4,u'4:飲みに行ける'),
                 (5,u'5:普通'),
                 (6,u'6:一緒に出かけたい'),
                 (7,u'7:すれ違ったら振り返る'),
                 (8,u'8:50人に一人の可愛さ'),
                 (9,u'9:100人に一人の可愛さ'),
                 (10,u'10:100人に一人の可愛さ'),
                 (11,u'カットモデル'),
                 (12,u'雑誌モデル'),
                 (13,u'女優並'),
                 (14,u'芸能人')
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