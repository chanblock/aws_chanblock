from email import message
from django.shortcuts import render
from django.http import HttpResponse
from assetModule.utils import userUtil
from django.contrib import messages
# Create your views here.
def comments(request):
    myDict = dict(request.POST)
    comment=userUtil.user_comment(myDict) 
    if comment:
       return HttpResponse(messages.success(request,"Commit saved successfully"))
    else:
        return HttpResponse(messages.error(request,"Commit not saved successfully"))

def comments_history(request):
    return render(request,"users/comments_history.html" )  