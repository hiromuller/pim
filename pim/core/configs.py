# -*- coding: utf-8 -*-
"""
URL設定
"""
PROGRESS_LATEST_PAGE_TITLE_URL = 'progress_latest/page_title.html'
PROGRESS_LATEST_MAIN_URL = 'progress_latest/main_content.html'
PROGRESS_LATEST_SUB_URL = 'progress_latest/sub_content.html'

PROGRESS_LIST_PAGE_TITLE_URL = 'progress_list/page_title.html'
PROGRESS_LIST_MAIN_URL = 'progress_list/main_content.html'
PROGRESS_LIST_SUB_URL = 'progress_list/sub_content.html'

TARGET_PAGE_TITLE_URL = 'target/page_title.html'
TARGET_MAIN_URL = 'target/main_content.html'
TARGET_SUB_URL = 'target/sub_content.html'

ACCOUNT_PAGE_TITLE_URL = 'account/page_title.html'
ACCOUNT_MAIN_URL = 'account/main_content.html'
ACCOUNT_SUB_URL = 'account/sub_content.html'

TOP_URL = '/main/'


"""
アクションの設定
"""
ACTION_PROGRESS_LATEST = 'progress_latest'
ACTION_PROGRESS_LIST = 'progress_list'
ACTION_PROGRESS_ADD = 'progress_add'
ACTION_TARGET_LIST = 'target'
ACTION_TARGET_ADD = 'target_add'
ACTION_ACCOUNT_LIST = 'account'

ACTION_TOP = ACTION_PROGRESS_LATEST

ACTION_DICT = {
                'ACTION_PROGRESS_LATEST':ACTION_PROGRESS_LATEST,
                'ACTION_PROGRESS_LIST':ACTION_PROGRESS_LIST,
                'ACTION_PROGRESS_ADD':ACTION_PROGRESS_ADD,
                'ACTION_TARGET_LIST':ACTION_TARGET_LIST,
                'ACTION_TARGET_ADD':ACTION_TARGET_ADD,
                'ACTION_ACCOUNT_LIST':ACTION_ACCOUNT_LIST,
                'ACTION_TOP':ACTION_TOP
               }
"""
コンテンツHTML
"""
PAGE_TITLE = '/page_title.html'
CONTENT_MAIN = '/main_content.html'
CONTENT_SUB = '/sub_content.html'