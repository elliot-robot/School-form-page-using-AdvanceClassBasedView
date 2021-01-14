from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView,ListView,DetailView
from . import models

class SchoolListView(ListView):
    #context_object_name = 'schools'
    model = models.School

def test(request):
    return render(request,'basic_app/test.html')


class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'

class hi(View):
    def get(self,request):
        return HttpResponse("Testing thing")



class IndexView(TemplateView):
    template_name = 'basic_app/index.html'
'''
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'BASIC INJECTION!'
        return context



class CBView(View):
    def get(self,request):
        return HttpResponse("CLASS BASED VIEWS ARE COOL!!")
# Create your views here.
#def index(request):
#    return render(request,'basic_app/index.html')
'''
