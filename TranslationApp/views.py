from django.shortcuts import render
from googletrans import Translator
from django.views import View

# Create your views here.


class translate(View):
    def get(self,request):
        return render(request, "translationapp/translate.html",{})


class translated(View):

    def post(self,request):
        text = request.POST.get("text")
        lang = request.POST.get("lang")


        translate = Translator()
        dt = translate.detect(text)
        dt2 = dt.lang
        translated = translate.translate(text,lang)
        tr = translated.text
        return render(request, "translationapp/translated.html", {"translated":tr})
