from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import train

#J'importe Random pour pouvoir utiliser un module qui va choisir un chiffre aléatoire entre 2 valeurs que je vais définir.
import random



def index(request):
    if 'recherche' in request.GET:
        train_numero = request.GET['recherche'] 
        # Mon redirect me permets de rediriger l'utilisateur vers la page profiltrain suivit du train_id qui représente le train_num qui est la valeur rentrée dans la barre.
        return redirect('profiltrain', train_id=train_numero)
    

    context = {
        "trains": train.objects.all(),
        "random": random.randint(1, 15),
        #J'ai déplacé ma ligne '"random": random.randint(1, 15),' dans context au lieu de la mettre en bas comme dans la fonction profiltrain,
        # car lorsque je rajoute un paramètre à mon "render" le html ne s'affiche plus correctement.
        
    }
    return render(request, "metroboomin/index.html", context)



def profiltrain(request, train_id) :
    listeTrain = train.objects.get(id = train_id)
    premierTrain = listeTrain
    random_id = random.randint(1, 15)

    return render(request, "metroboomin/profiltrain.html", {
        "id" : premierTrain.id,
        "datetime" : premierTrain.datetime,
        "destination" : premierTrain.destination,
        "plan" : premierTrain.plan,
        "nextID" : int(train_id) + 1,
        "random" : random_id,
    })