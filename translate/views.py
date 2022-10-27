# DJANGO MODULES
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse

# TRANSLATOR MODULES
from googletrans import Translator


# translate Text APIs
@api_view(['GET', 'POST'])
def translate_text_api(request):
    #payload
    original_text = request.data['text']
    source= request.data['from']
    destination = request.data['to']
    
    # Will check for the language and if it is not english 
    translator = Translator()
    text = str(translator.translate(original_text, src=source,dest=destination).text)
    
    return JsonResponse({"text":text})