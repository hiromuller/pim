from django.shortcuts import render
from django.core.context_processors import csrf

# Create your views here.
def show(request):
    if request.method == "POST":
        action = request.POST["action"]
    else:
        action = "progress_latest"
        
    main_url = '/main/'
    main_content = action + '/main_content.html'
    sub_content = action + '/sub_content.html'
    
    c = {}    
    url_dict = {'main_url':main_url, 
                'main_content':main_content,
                'sub_content':sub_content}
    c.update(csrf(request))
    c.update(url_dict)
    return render(request, 'common/main.html', c)