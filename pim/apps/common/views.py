from django.shortcuts import render

# Create your views here.
def logged_in(request):
    context = {}
    template = 'logged_in.html'
    return render(request, template, context)

def done(request):
    context = {}
    template = 'done.html'
    return render(request, template, context)

def logout(request):
    context = {}
    template = 'done.html'
    return render(request, template, context)
