# django
from django import forms
# third
# own
from apps.slider.models import Slider

class SliderForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = (
            "slug",
            "image"
        )
        labels = {
            'slug': 'Slug de la imagen',
            'image': 'Imagen del slider'
        }

    def __init__(self, *args, **kwargs):
        '''
                Esta funcion se encarga de darle el diseño al formulario.
                :param args: La cantidad de argumentos que recibe.
                :param kwargs: Se encarga de tomar los parametros de la url.
                '''
        super(SliderForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})