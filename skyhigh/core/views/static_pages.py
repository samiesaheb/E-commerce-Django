from django.shortcuts import render

def privacy_policy_view(request):
    return render(request, 'core/privacy_policy.html')

def terms_and_conditions_view(request):
    return render(request, 'core/terms_and_conditions.html')
