from django.shortcuts import render


def Home(request):
    '''
    This function gets executed upon calling for any gcname.
    '''
    context = {
        'title': 'Home'
        }
    return render(request, 'tm_web_app/home.html', context)