from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Societe(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=45)
    type = models.CharField(max_length=45)
    domaine = models.CharField(max_length=45)
    tel1 = models.CharField(max_length=45)
    tel2 = models.CharField(max_length=45, null=True, blank=True)
    fax = models.CharField(max_length=45, null=True, blank=True)
    email = models.CharField(max_length=45)

    def __str__(self):
        return self.nom


class Personne(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=45)
    prenom = models.CharField(max_length=45)
    adresse = models.CharField(max_length=45)
    gsm = models.CharField(max_length=10)
    tel = models.CharField(max_length=10, null=True, blank=True)
    email = models.CharField(max_length=45)
    profession = models.CharField(max_length=45, null=True, blank=True)
    societe = modelsForeignKey(Societe, on_delete=models.CASCADE, null=True, blank=True)
    poste_societe = models.CharField(max_length=45, null=True, blank=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    societe = models.ForeignKey(Societe, on_delete=models.CASCADE, null=True, blank=True)
    personne = models.ForeignKey(Societe, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f"Client: {self.personne.nom}"



class Agent(models.Model):
    id = models.AutoField(primary_key=True)
    code_agent = models.CharField(max_length=45)
    personne = models.ForeignKey(Personne, on_delete=models.CASCADE)

    def __str__(self):
        return f"Agent: {self.code_agent}"



class Prestation(models.Model):
    id = models.AutoField(primary_key=True)
    type_prestation = models.CharField(max_length=255)
    code_prestation = models.CharField(max_length=255)

    def __str__(self):
        return self.type_prestation



class Ouvrage(models.Model):
    id = models.AutoField(primary_key=True)
    type_ouvrage = models.CharField(max_length=45)
    code_ouvrage = models.CharField(max_length=45)

    def __str__(self):
        return self.type_ouvrage



def generate_fsn():
    year = datetime.now().year % 100
    count = FicheDeSuivi.objects.filter(fsn__endswith=f"/{year}").count() + 1
    return f"{count:03}/{year}"


class FicheDeSuivi(models.Model):
    id = models.AutoField(primary_key=True)
    fsn = models.CharField(max_length=20, unique=True, default=generate_fsn)
    projet = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)
    prestation = models.ForeignKey(Prestation, on_delete=models.CASCADE)
    ouvrage = models.ForeignKey(Ouvrage, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateField()
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)

    def __str__(self):
        return self.fsn



