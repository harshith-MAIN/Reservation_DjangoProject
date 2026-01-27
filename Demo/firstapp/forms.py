from django import Form
from .models import Reservation

class Reservation(Form.ModelForm):
    class Meta:
        moodel = Reservation
        fields = '__all__'