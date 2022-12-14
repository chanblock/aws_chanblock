from django.http import HttpResponse
from urllib import request
from django.shortcuts import render,redirect
from .utils import assetsUtil,userUtil
from django.http import JsonResponse
from django.contrib import messages


def home(request):
  return render(request, 'services/home.html')

def maintenance(request):  
  return render(request, 'maintenance.html')

def register_email(request):  
    print('tipo de peticion',request.META.get('HTTP_X_REQUESTED_WITH'))
    if request.META.get('HTTP_X_REQUESTED_WITH')=='XMLHttpRequest':
        userUtil.register_email_ajax(request)
        response = {
          'msg':'Your email has been submitted successfully' # response message
        }    
        return JsonResponse(response)
    else:
        aux =userUtil.register_email(request)
        if aux:    
            return redirect(home)
        else:
            return redirect(form_register_email)

def form_register_email(request): 
  return render(request, 'register.html')

def getAssets(request):
  listMetric= assetsUtil.getAssets() 
  return render(request, 'assets/indicators.html',{'assets': listMetric})

def coin_detail(request,symbol):
  coin_detail= assetsUtil.coin_detail(symbol)
  print(coin_detail.get('div'))
  return render(request, 'assets/coin_detail.html',{'coin_detail': coin_detail})

def graph_default(request):
  context= assetsUtil.graph('btc')
  print('context view.graficos: ',context.keys())
  return render(request, 'assets/graphics.html', context)
  
def graphics(request):
  myDict = dict(request.POST)
  print('dict of graph',myDict)
  context= assetsUtil.graph(myDict)
  msg=''
  print('view.graphics: context: ',context['message'])
  if len(context['message']) !=0:  
    for strmsg in context['message']:
       msg = strmsg+' '+msg      
    msg_error = "No results found: "+msg
    messages.error(request, msg_error)
    if context['exist_plot']:  
      return render(request, 'graphics.html', context)
    else:
      return redirect('graph_default')  
  print('--++++++++++',context.keys())
  return HttpResponse(context.values())

def gridGraphics(request):
  myDict = dict(request.POST)
  print('dict of gridgraph1',myDict)
  context= assetsUtil.grid_graph(myDict)
  print('key para graph 2',context.keys())
  return HttpResponse(context.values())
  # return HttpResponse({context.get('div1'),context.get('script1'),context.get('dataGraph1')})

def gridGraphics2(request):
  myDict = dict(request.POST)
  print('dict of gridgraph2',myDict)
  context= assetsUtil.grid_graph(myDict)
  print('key para graph 3',context.keys())
  return HttpResponse(context.values())
  # return HttpResponse({context.get('div2'),context.get('script2'),context.get('dataGraph2')})