from django.shortcuts import render, redirect
from googletrans import Translator
from django.http import HttpResponse


def translator(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        lang = request.POST.get('lang')
        print('text:', text, 'lang:', lang)
        # translate the language
        translator = Translator(service_urls=['translate.googleapis.com'])

        # detect the language
        dt = translator.detect(text)
        dt2 = dt.lang
        translated = translator.translate(text, lang)
        tr = translated.text
        content = {
            'translated': tr,'u_lang': dt2,'t_lang':lang
        }
        return render(request,'translator_app/translated.html', content)
    return render(request, 'translator_app/translator.html')


# Create your views here.
def translated(request):

    text = request.GET.get('text')
    lang = request.GET.get('lang')
    print('text:', text, 'lang:', lang)
    #translate the language
    translator= Translator(service_urls=['translate.googleapis.com'])

    #detect the language
    dt=translator.detect(text)
    dt2=dt.lang
    translated=translator.translate(text,lang)
    tr=translated.text
    return render(request,'translated.html',{'translated': tr,'u_lang': dt2,'t_lang':lang})