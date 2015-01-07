# -*- coding: utf-8 -*-
'''
Created on 2014/07/23

@author: h-nagata
'''
from django.db import transaction
import common.models as MODELS
import consts as CONSTS
from django.db.models import Q

def getUserByLoginId(username):
    user = MODELS.User.objects.filter(username = username)
    if user.count() == 1:
        return user.first().encode()
    else:
        return None

def hasAgreement(user):
    """
    情報取り扱い同意書に同意しているか確認する
    return boolean
    """
    result = MODELS.Statement_Agreement.objects.filter(user=user,
                                                       agreement=True,
                                                       statement__pk=CONSTS.INFORMATION_HANDLING_AGREEMENT_ID)

    if len(result) > 0:
        return True
    else:
        return False

def selectStatement(statement_id):
    """
    承諾書を返却する
    return statement
    """
    statement = MODELS.Statement.objects.filter(pk = statement_id)
    if len(statement) == 1:
        return statement[0]
    else:
        return None

@transaction.commit_on_success()
def addAgreement(user, statement_id):
    """
    承諾する
    """
    statement = MODELS.Statement.objects.get(pk=statement_id)
    statement_agreement = MODELS.Statement_Agreement()
    statement_agreement.user = user
    statement_agreement.agreement = True
    statement_agreement.statement = statement
    statement_agreement.save()

class QuerySetUtil():
    '''
    django QuerySet操作補助関連のUtilを集めたクラス
    '''
    @classmethod
    def getKeywordSearchFilterArgsAll(self, model, model_str, keyword):
        queries = []
        for f in model._meta.fields:
            if model._meta.get_field(f.name).get_internal_type() in ['CharField', 'TextField'] :
                kwargs = {str('%s__%s__contains' % (model_str, f.name)) : keyword}
                queries.append(Q(**kwargs))

        query = queries.pop()
        for item in queries:
            query |= item
        return query