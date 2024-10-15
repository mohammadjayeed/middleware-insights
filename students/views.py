from django.shortcuts import render
from django.template.response import TemplateResponse

def set(request):
    # raise Exception("set raised an exception")
    print('I am the view in between middlewares')
    response = TemplateResponse(request,'students/home.html',{'name':'jayeed'})
    return response
