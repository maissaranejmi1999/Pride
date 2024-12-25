from django import forms
from .models import Societe, Personne, Client, Agent, Prestation, Ouvrage, FicheDeSuivi


class SocieteForm(forms.Modelform):
    class Meta:
        model = Societe
        fields = '__all__'



class PersonneForm(forms.Modelform):
    class Meta:
        model = Personne
        fields = '__all__'



class ClientForm(forms.Modelform):
    class Meta:
        model = Client
        fields = '__all__'



class AgentForm(forms.Modelform):
    class Meta:
        model = Agent
        fields = '__all__'



class PrestationForm(forms.ModelForm):
    class Meta:
        model = Prestation
        fields = '__all__'



class OuvrageForm(forms.ModelForm):
    class Meta:
        model = Ouvrage
        fields = '__all__'



class FicheDeSuiviForm(forms.ModelForm):
    class Meta:
        model = FicheDeSuivi
        fields = ['project', 'adresse', 'prestation', 'ouvrage', 'client', 'date', 'agent']
        