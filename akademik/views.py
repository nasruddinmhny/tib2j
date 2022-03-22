from multiprocessing import context
from django.shortcuts import render,HttpResponse

# Create your views here.
def manage_akademik(request):
    title = 'Halaman Akademik'
    context={
        'title':title,
    }
    return render(request,'manage_akademik_template.html', context)

def edit_akademik(request):
    return HttpResponse('<h2>Halam Edit</h2>')

def data_akademik(request):

    title = 'Data Akademik'

    context = {

        'title':title,

    }
    return render(request,'index.html', context)