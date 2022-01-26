from django.shortcuts import render


def kis_base_landing(request):
    return render(request, 'kis_base_landing.html', {})
