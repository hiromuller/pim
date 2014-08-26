from django.shortcuts import render
from django.core.context_processors import csrf
import configs as CONFIG
import forms as FORMS
import services as SERVICES
import messages as MSGS

# targetlist views

def index(request):
    addForm = FORMS.TargetForm()
    forms = {'addForm':addForm}
    c = {}    
    c.update(forms)
    return show(request, c)
    
def add(request):
    if request.method == 'POST':
        result = SERVICES.addTarget(request)
        if not result == 'success':
            fail_form = FORMS.TargetForm(request.POST)
            c = {'addForm':fail_form}
            c.update({'form_message':MSGS.ADD_FAIL})
            return show(request, c)
    c = {'form_message': MSGS.ADD_SUCCESS}
    c.update({'addForm':FORMS.TargetForm()})
    return show(request, c)

def show(request, c):
    print 'target_list'    
    main_url = CONFIG.TOP_URL
    page_title = CONFIG.TARGET_LIST_PAGE_TITLE_URL
    main_content = CONFIG.TARGET_LIST_MAIN_URL
    sub_content = CONFIG.TARGET_LIST_SUB_URL

    url_dict = {'main_url':main_url, 
                'page_title':page_title, 
                'main_content':main_content,
                'sub_content':sub_content}
    c.update(csrf(request))
    c.update(url_dict)
    c.update(CONFIG.ACTION_DICT)
    return render(request, 'common/main.html', c)
    