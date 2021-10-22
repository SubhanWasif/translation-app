from django.shortcuts import render
import Translator

# Create your views here.


def translate(request):
    return render(request, "translationapp/translate.html",{})


def translated(request):
    text = request.GET.get("text")
    lang = request.GET.get("lang")


    translate = Translator()
    dt = translate.detect(text)
    dt2 = dt.lang
    translated = translate.translate(text,lang)
    tr = translated.text




    return render(request, "translationapp/translated.html",{"translated":translated})
