 # Использование шаблонов (2 подход - простой)
from django.shortcuts import render
# Использование шаблонов (1 подход - сложный)
# from django.http import HttpResponse
# from django.template import loader

from .models import Bb

def index(request):
    # Использование шаблонов (2 подход - простой)
    bbs = Bb.objects.order_by('-published')
    context = {'bbs':bbs}
    return render(request, 'bboard\index.html', context)
    # Использование шаблонов (1 подход - сложный)
    # template = loader.get_template('bboard/index.html')
    # bbs = Bb.objects.order_by('-published')
    # context = {'bbs':bbs}
    # return HttpResponse(template.render(context, request))


    # Вывод данных напрямую
    # s = 'List of bills\r\n\r\n\r\n'
    # for bb in Bb.objects.order_by('-published'):
    #     s += bb.title + '\r\n' + bb.content + '\r\n\r\n'
    # return HttpResponse(s, content_type = 'text/plain; charset=utf-8')

    # return HttpResponse('Site under constraction... Когда-то у меня была такая надпись на сайте =)')

# Create your views here.
