import forms as FORMS

def addTarget(request):
    new_target_form = FORMS.TargetForm(request.POST)
    if new_target_form.is_valid():
        new_target_form.save()
