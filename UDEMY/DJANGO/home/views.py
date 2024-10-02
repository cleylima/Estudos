from django.shortcuts import render

# Create your views here.



def Home(request):
    print('home')

    context = {'text': 'Olá Home'}
    return render(request, 'home/index.html', context)