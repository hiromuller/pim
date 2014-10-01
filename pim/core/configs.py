# -*- coding: utf-8 -*-
"""
URL設定
"""
HOME_PAGE_TITLE_URL = 'home/page_title.html'
HOME_MAIN_URL = 'home/main_content.html'
HOME_SUB_URL = 'home/sub_content.html'

PROGRESS_PAGE_TITLE_URL = 'progress/page_title.html'
PROGRESS_MAIN_URL = 'progress/main_content.html'
PROGRESS_SUB_URL = 'progress/sub_content.html'

TARGET_PAGE_TITLE_URL = 'target/page_title.html'
TARGET_MAIN_URL = 'target/main_content.html'
TARGET_SUB_URL = 'target/sub_content.html'
TARGET_DETAIL = 'target/target_detail.html'

ACCOUNT_PAGE_TITLE_URL = 'account/page_title.html'
ACCOUNT_MAIN_URL = 'account/main_content.html'
ACCOUNT_SUB_URL = 'account/sub_content.html'

TEAM_PAGE_TITLE_URL = 'team/page_title.html'
TEAM_MAIN_URL = 'team/main_content.html'
TEAM_SUB_URL = 'team/sub_content.html'

HELP_PAGE_TITLE_URL = 'help/page_title.html'
HELP_MAIN_URL = 'help/main_content.html'
HELP_SUB_URL = 'help/sub_content.html'

MANUAL_PAGE_TITLE_URL = 'manual/page_title.html'
MANUAL_MAIN_URL = 'manual/main_content.html'
MANUAL_SUB_URL = 'manual/sub_content.html'


TOP_URL = '/main/'


"""
アクションの設定
"""
ACTION_HOME = 'home'
ACTION_PROGRESS_LIST = 'progress_list'
ACTION_PROGRESS_ADD = 'progress_add'
ACTION_PROGRESS_UPDATE = 'progress_update'
ACTION_TARGET_LIST = 'target'
ACTION_TARGET_ADD = 'target_add'
ACTION_TARGET_DETAIL = "target_detail"
ACTION_TARGET_UPDATE = 'target_update'
ACTION_ACCOUNT = 'account'
ACTION_ACCOUNT_UPDATE = 'account_update'
ACTION_TEAM = 'team'
ACTION_TEAM_ADD = 'team_add'
ACTION_TEAM_INVITE = 'team_invite'
ACTION_TEAM_INVITE_ACCEPT_USER = 'team_invite_accept_user'
ACTION_TEAM_INVITE_ACCEPT_TEAM = 'team_invite_accept_team'
ACTION_TEAM_DELETE_MEMBER = 'team_delete_member'
ACTION_TEAM_DELETE_TEAM = 'team_delete_team'
ACTION_HELP = 'help'
ACTION_MANUAL = 'manual'


ACTION_DICT = {
                'ACTION_HOME':ACTION_HOME,
                'ACTION_PROGRESS_LIST':ACTION_PROGRESS_LIST,
                'ACTION_PROGRESS_ADD':ACTION_PROGRESS_ADD,
                'ACTION_PROGRESS_UPDATE':ACTION_PROGRESS_UPDATE,
                'ACTION_TARGET_LIST':ACTION_TARGET_LIST,
                'ACTION_TARGET_ADD':ACTION_TARGET_ADD,
                'ACTION_TARGET_DETAIL':ACTION_TARGET_DETAIL,
                'ACTION_TARGET_UPDATE': ACTION_TARGET_UPDATE,
                'ACTION_ACCOUNT':ACTION_ACCOUNT,
                'ACTION_ACCOUNT_UPDATE':ACTION_ACCOUNT_UPDATE,
                'ACTION_TEAM':ACTION_TEAM,
                'ACTION_TEAM_ADD':ACTION_TEAM_ADD,
                'ACTION_TEAM_INVITE':ACTION_TEAM_INVITE,
                'ACTION_TEAM_INVITE_ACCEPT_USER':ACTION_TEAM_INVITE_ACCEPT_USER,
                'ACTION_TEAM_INVITE_ACCEPT_TEAM':ACTION_TEAM_INVITE_ACCEPT_TEAM,
                'ACTION_TEAM_DELETE_MEMBER':ACTION_TEAM_DELETE_MEMBER,
                'ACTION_TEAM_DELETE_TEAM':ACTION_TEAM_DELETE_TEAM,
                'ACTION_HELP':ACTION_HELP,
                'ACTION_MANUAL':ACTION_MANUAL
               }
"""
コンテンツHTML
"""
PAGE_TITLE = '/page_title.html'
CONTENT_MAIN = '/main_content.html'
CONTENT_SUB = '/sub_content.html'
