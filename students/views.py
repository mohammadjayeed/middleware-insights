from django.shortcuts import render

def set(request):
    print('I am the view in between middlewares')
    response = render(request,'students/home.html')
    return response
