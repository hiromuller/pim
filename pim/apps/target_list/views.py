from django.shortcuts import render
from django.core.context_processors import csrf
import configs as CONFIG
import forms as FORMS
import services as SERVICES

# targetlist views

def index(request):
    addForm = FORMS.TargetForm()
    
    print 'target_list'    
    main_url = CONFIG.TOP_URL
    page_title = CONFIG.TARGET_LIST_PAGE_TITLE_URL
    main_content = CONFIG.TARGET_LIST_MAIN_URL
    sub_content = CONFIG.TARGET_LIST_SUB_URL
    forms = {'addForm':addForm}
    c = {}    
    url_dict = {'main_url':main_url, 
                'page_title':page_title, 
                'main_content':main_content,
                'sub_content':sub_content}
    action_dict = CONFIG.ACTION_DICT
    c.update(csrf(request))
    c.update(url_dict)
    c.update(forms)
    c.update(action_dict)
    return render(request, 'common/main.html', c)
    
def add(request):
    if request.method == 'POST':
        SERVICES.addTarget(request)
    return index(request)