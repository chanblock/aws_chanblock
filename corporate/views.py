from django.shortcuts import render
from assetModule.utils import assetsUtil,userUtil
from django.http import JsonResponse
from django.shortcuts import render,redirect

# Create your views here.
def home(request):
  return render(request, 'services/home.html')

def services(request):   
  return render(request, 'services/services.html')

def regulation(request):    
  return render(request, 'services/regulation.html')

def education(request):    
  return render(request, 'services/education.html')

def monitoring(request):    
  return render(request, 'services/monitoring.html')

def maintenance(request):  
  return render(request, 'services/maintenance.html')

def monitorMtGox(request): 
  context= assetsUtil.home()
  print(context.keys())  
  return render(request, 'services/monitorMtGox.html',context)

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