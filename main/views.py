from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def index(request):
    context = {
        'title': 'Home',
        'content': 'Welcome to WordGuesserWeb!'
    }

    return render(request, 'main/index.html', context)
