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

TARGET_DETAIL_PAGE_TITLE_URL = 'target_detail/page_title.html'
TARGET_DETAIL_MAIN_URL = 'target_detail/main_content.html'
TARGET_DETAIL_SUB_URL = 'target_detail/sub_content.html'

TARGET_LIST_PAGE_TITLE_URL = 'target_list/page_title.html'
TARGET_LIST_MAIN_URL = 'target_list/main_content.html'
TARGET_LIST_SUB_URL = 'target_list/sub_content.html'

USER_DETAIL_PAGE_TITLE_URL = 'user_detail/page_title.html'
USER_DETAIL_MAIN_URL = 'user_detail/main_content.html'
USER_DETAIL_SUB_URL = 'user_detail/sub_content.html'

USER_LIST_PAGE_TITLE_URL = 'user_list/page_title.html'
USER_LIST_MAIN_URL = 'user_list/main_content.html'
USER_LIST_SUB_URL = 'user_list/sub_content.html'

TOP_URL = '/main/'


"""
アクションの設定
"""
ACTION_PROGRESS_LATEST = 'progress_latest'
ACTION_PROGRESS_LIST = 'progress_list'
ACTION_TARGET_DETAIL = 'target_detail'
ACTION_TARGET_LIST = 'target_list'
ACTION_TARGET_ADD = 'target_add'
ACTION_USER_DETAIL = 'user_detail'
ACTION_USER_LIST = 'user_list'

ACTION_TOP = ACTION_PROGRESS_LATEST

ACTION_DICT = {
                'ACTION_PROGRESS_LATEST':ACTION_PROGRESS_LATEST,
                'ACTION_PROGRESS_LIST':ACTION_PROGRESS_LIST,
                'ACTION_TARGET_DETAIL':ACTION_TARGET_DETAIL,
                'ACTION_TARGET_LIST':ACTION_TARGET_LIST,
                'ACTION_TARGET_ADD':ACTION_TARGET_ADD,
                'ACTION_USER_DETAIL':ACTION_USER_DETAIL,
                'ACTION_USER_LIST':ACTION_USER_LIST,
                'ACTION_TOP':ACTION_TOP
               }
"""
コンテンツHTML
"""
PAGE_TITLE = '/page_title.html'
CONTENT_MAIN = '/main_content.html'
CONTENT_SUB = '/sub_content.html'