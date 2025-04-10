# django
from django.shortcuts import render
from django.views.generic.base import View
# third
# own
from apps.slider.models import Slider

# Create your views here.

class Home(View):
    '''Esta clase se encarga de mostrar la plantilla de inicio o landing page sin logeo.'''
    template_name = 'home.html'

    def get(self, request):
        '''
                    Esta funcion se encarga de mostrar todos los sliders.
                    :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
                    :return: Nos retorna la plantilla de inicio y todos los sliders registrados en el sistema.
                    '''
        sliders = Slider.objects.all()
        return render(request, self.template_name, {'sliders': sliders})