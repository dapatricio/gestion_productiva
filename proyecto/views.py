from django.shortcuts import render
from django.shortcuts import render_to_response, RequestContext
from django.template import Context, loader
from .models import *
from django.utils.encoding import smart_unicode, force_unicode, smart_str

# Create your views here.
def index(request):
    return render(request, 'index.html', context_instance=RequestContext(request))

def contacto(request):
    return render(request, 'contacto.html', context_instance=RequestContext(request))    

def mapa(request):

    id_tipo= Tipo.objects.all()
    total_provincias=Provincia.objects.all()
    lista_disc=[]
    contador=0
    Azuay=0
    Bolivar=0
    Canar=0
    Carchi=0
    Cotopaxi=0
    Chimborazo=0
    El_Oro=0
    Esmeraldas=0
    Guayas=0
    Imbabura=0
    Loja=0
    Los_Rios=0
    Manabi=0
    Morona_Santiago=0
    Napo=0
    Pastaza=0
    Pichincha=0
    Tungurahua=0
    Zamora_Chinchipe=0
    Galapagos=0     
    Sucumbios=0   
    Orellana=0  
    Santo_Domingo=0    
    Santa_Elena=0   

    if request.method == "POST":
        valor=request.POST.get("selProv")
        for p in total_provincias:
            discapacidades=Parrodis.objects.filter(id_parroquia__id_canton__id_provincia__pk=p.pk,id_discapacidad__id_tipo__id_tipo=int(valor))
            
            for d in discapacidades:
                contador=contador+d.id_discapacidad.si

            if p.nombre_proncia == 'Azuay':
                Azuay=contador
            if p.nombre_proncia=='Bolivar':
                Bolivar=contador
            if p.nombre_proncia=='Canar':
                Canar=contador   
            if p.nombre_proncia=='Carchi':
                Carchi=contador      
            if p.nombre_proncia=='Cotopaxi':
                Cotopaxi=contador 
            if p.nombre_proncia=='Chimborazo':
                Chimborazo=contador     
            if p.nombre_proncia=='El Oro':
                El_Oro=contador     
            if p.nombre_proncia=='Esmeraldas':
                Esmeraldas=contador 
            if p.nombre_proncia=='Guayas':
                Guayas=contador 
            if p.nombre_proncia=='Imbabura':
                Imbabura=contador     
            if p.nombre_proncia=='Loja':
                Loja=contador     
            if p.nombre_proncia=='Los Rios':
                Los_Rios=contador 
            if p.nombre_proncia=='Manabi':
                Manabi=contador     
            if p.nombre_proncia=='Morona Santiago':
                Morona_Santiago=contador     
            if p.nombre_proncia=='Napo':
                Napo=contador     
            if p.nombre_proncia=='Pastaza':
                Pastaza=contador     
            if p.nombre_proncia=='Pichincha':
                Pichincha=contador     
            if p.nombre_proncia=='Tungurahua':
                Tungurahua=contador     
            if p.nombre_proncia=='Zamora Chinchipe':
                Zamora_Chinchipe=contador     
            if p.nombre_proncia=='Galapagos':
                Galapagos=contador     
            if p.nombre_proncia=='Sucumbios':
                Sucumbios=contador     
            if p.nombre_proncia=='Orellana':
                Orellana=contador     
            if p.nombre_proncia=='Santo Domingo':
                Santo_Domingo=contador     
            if p.nombre_proncia=='Santa Elena':
                Santa_Elena=contador     


            contador=0

    tipo={"id_tipo":id_tipo,"Manabi":Manabi,"Morona_Santiago":Morona_Santiago,"Pastaza":Pastaza,
    "Napo":Napo,"Pichincha":Pichincha,"Tungurahua":Tungurahua,"Azuay":Azuay,"Bolivar":Bolivar,
    "Zamora_Chinchipe":Zamora_Chinchipe,"Galapagos":Galapagos,"Sucumbios":Sucumbios,"Canar":Canar,
    "Orellana":Orellana,"Santo_Domingo":Santo_Domingo,"Santa_Elena":Santa_Elena,"Los_Rios":Los_Rios,
    "Loja":Loja,"Imbabura":Imbabura,"Guayas":Guayas,"Esmeraldas":Esmeraldas,"El_Oro":El_Oro,
    "Chimborazo":Chimborazo,"Cotopaxi":Cotopaxi,"Carchi":Carchi}
    # obtengo las parroquias de un canton
    return render(request, 'mapa.html', tipo ,context_instance=RequestContext(request))  

def mental(request):

    id_provincia= Provincia.objects.all()
    preescolar=0
    centro=0
    ninguno=0
    primario=0
    secundario=0
    basica=0
    bachillerato=0
    superior=0
    postbachillerato=0
    id_canton={}
    nombre_canton={}

    pobla={}
    tipo={"id_provincia":id_provincia} 

    if request.method == "POST":
        if "form1" in request.POST:
            valor2=request.POST["selProv2"]
            pobla=Cantpob.objects.filter(id_canton__id_provincia__pk=int(valor2),id_poblacion5anios__id_tipo__id_tipo=2)

        for d in pobla: 
            preescolar=d.id_poblacion5anios.preescolar 
            centro=d.id_poblacion5anios.centro
            ninguno=d.id_poblacion5anios.ninguno
            primario=d.id_poblacion5anios.primario
            secundario=d.id_poblacion5anios.secundario
            basica=d.id_poblacion5anios.basica
            bachillerato=d.id_poblacion5anios.bachillerato
            superior=d.id_poblacion5anios.superior
            postbachillerato=d.id_poblacion5anios.postbachillerato

    tipo={"id_provincia":id_provincia,"preescolar":preescolar,"centro":centro,"ninguno":ninguno,
    "primario":primario,"secundario":secundario,"basica":basica,"bachillerato":bachillerato,
    "superior":superior, "postbachillerato":postbachillerato}
    # obtengo las parroquias de un canton
    return render(request, 'mental.html', tipo ,context_instance=RequestContext(request))  
def visual(request):

    id_provincia= Provincia.objects.all()
    preescolar=0
    centro=0
    ninguno=0
    primario=0
    secundario=0
    basica=0
    bachillerato=0
    superior=0
    postbachillerato=0
    tipo={"id_provincia":id_provincia} 
    if request.method == "POST":
        valor2=request.POST["selProvVis"]
        pobla=Cantpob.objects.filter(id_canton__id_provincia__pk=int(valor2),id_poblacion5anios__id_tipo__id_tipo=4)
        
        for d in pobla: 
            preescolar=d.id_poblacion5anios.preescolar 
            centro=d.id_poblacion5anios.centro
            ninguno=d.id_poblacion5anios.ninguno
            primario=d.id_poblacion5anios.primario
            secundario=d.id_poblacion5anios.secundario
            basica=d.id_poblacion5anios.basica
            bachillerato=d.id_poblacion5anios.bachillerato
            superior=d.id_poblacion5anios.superior
            postbachillerato=d.id_poblacion5anios.postbachillerato

    tipo={"id_provincia":id_provincia,"preescolar":preescolar,"centro":centro,"ninguno":ninguno,
    "primario":primario,"secundario":secundario,"basica":basica,"bachillerato":bachillerato,
    "superior":superior, "postbachillerato":postbachillerato}
    # obtengo las parroquias de un canton
    return render(request, 'visual.html', tipo ,context_instance=RequestContext(request))  
def auditiva(request):

    id_provincia= Provincia.objects.all()
    preescolar=0
    centro=0
    ninguno=0
    primario=0
    secundario=0
    basica=0
    bachillerato=0
    superior=0
    postbachillerato=0
    tipo={"id_provincia":id_provincia} 
    if request.method == "POST":
        valor2=request.POST["selProvAudi"]
        pobla=Cantpob.objects.filter(id_canton__id_provincia__pk=int(valor2),id_poblacion5anios__id_tipo__id_tipo=3)
        
        for d in pobla: 
            preescolar=d.id_poblacion5anios.preescolar 
            centro=d.id_poblacion5anios.centro
            ninguno=d.id_poblacion5anios.ninguno
            primario=d.id_poblacion5anios.primario
            secundario=d.id_poblacion5anios.secundario
            basica=d.id_poblacion5anios.basica
            bachillerato=d.id_poblacion5anios.bachillerato
            superior=d.id_poblacion5anios.superior
            postbachillerato=d.id_poblacion5anios.postbachillerato

    tipo={"id_provincia":id_provincia,"preescolar":preescolar,"centro":centro,"ninguno":ninguno,
    "primario":primario,"secundario":secundario,"basica":basica,"bachillerato":bachillerato,
    "superior":superior, "postbachillerato":postbachillerato}
    # obtengo las parroquias de un canton
    return render(request, 'auditiva.html', tipo ,context_instance=RequestContext(request))  

def fisica(request):

    id_provincia= Provincia.objects.all()
    preescolar=0
    centro=0
    ninguno=0
    primario=0
    secundario=0
    basica=0
    bachillerato=0
    superior=0
    postbachillerato=0
    tipo={"id_provincia":id_provincia} 
    if request.method == "POST":
        valor2=request.POST["selProvFisica"]
        pobla=Cantpob.objects.filter(id_canton__id_provincia__pk=int(valor2),id_poblacion5anios__id_tipo__id_tipo=5)
        
        for d in pobla: 
            preescolar=d.id_poblacion5anios.preescolar 
            centro=d.id_poblacion5anios.centro
            ninguno=d.id_poblacion5anios.ninguno
            primario=d.id_poblacion5anios.primario
            secundario=d.id_poblacion5anios.secundario
            basica=d.id_poblacion5anios.basica
            bachillerato=d.id_poblacion5anios.bachillerato
            superior=d.id_poblacion5anios.superior
            postbachillerato=d.id_poblacion5anios.postbachillerato

    tipo={"id_provincia":id_provincia,"preescolar":preescolar,"centro":centro,"ninguno":ninguno,
    "primario":primario,"secundario":secundario,"basica":basica,"bachillerato":bachillerato,
    "superior":superior, "postbachillerato":postbachillerato}
    # obtengo las parroquias de un canton
    return render(request, 'fisica.html', tipo ,context_instance=RequestContext(request))      

def intelectual(request):

    id_provincia= Provincia.objects.all()
    preescolar=0
    centro=0
    ninguno=0
    primario=0
    secundario=0
    basica=0
    bachillerato=0
    superior=0
    postbachillerato=0
    tipo={"id_provincia":id_provincia} 
    if request.method == "POST":
        valor2=request.POST["selProvIntel"]
        pobla=Cantpob.objects.filter(id_canton__id_provincia__pk=int(valor2),id_poblacion5anios__id_tipo__id_tipo=6)
        
        for d in pobla: 
            preescolar=d.id_poblacion5anios.preescolar 
            centro=d.id_poblacion5anios.centro
            ninguno=d.id_poblacion5anios.ninguno
            primario=d.id_poblacion5anios.primario
            secundario=d.id_poblacion5anios.secundario
            basica=d.id_poblacion5anios.basica
            bachillerato=d.id_poblacion5anios.bachillerato
            superior=d.id_poblacion5anios.superior
            postbachillerato=d.id_poblacion5anios.postbachillerato

    tipo={"id_provincia":id_provincia,"preescolar":preescolar,"centro":centro,"ninguno":ninguno,
    "primario":primario,"secundario":secundario,"basica":basica,"bachillerato":bachillerato,
    "superior":superior, "postbachillerato":postbachillerato}
    # obtengo las parroquias de un canton
    return render(request, 'intelectual.html', tipo ,context_instance=RequestContext(request))        

def analfabetismo(request):

    id_provincia= Provincia.objects.all() 
    alfabeto=0
    analfabeto=0
    tipo={"id_provincia":id_provincia}     
    if request.method == "POST":
        valor7=request.POST.get("selProv7")
        analfabetismo=Analfabestismo.objects.filter(id_parroquia__id_canton__id_provincia__pk=int(valor7))
        for a in analfabetismo:
            analfabeto=a.analfabeto
            alfabeto=a.alfabeto

    tipo={"id_provincia":id_provincia,"analfabeto":analfabeto, "alfabeto":alfabeto}
    return render(request, 'analfabetismo.html', tipo ,context_instance=RequestContext(request))

def provincias(request):
    
    # obtengo las provincias
    id_provincia= Provincia.objects.all();

    provincia={"id_provincia":id_provincia}

    return render(request, 'mapa.html', provincia ,context_instance=RequestContext(request))

def cantones(request):
    
    # obtengo los cantones de una provincia

    id_canton= Canton.objects.all();

    canton={"id_canton":id_canton}

    return render(request, 'listado_cantones.html', canton ,context_instance=RequestContext(request))

def parroquias(request): 
    

    id_parroquia= Parroquia.objects.all();

    parroquia={"id_parroquia":id_parroquia}
    # obtengo las parroquias de un canton
    return render(request, 'listado_parroquias.html', parroquia ,context_instance=RequestContext(request))    


def parroquias(request): 
    

    id_parroquia= Parroquia.objects.all();

    parroquia={"id_parroquia":id_parroquia}
    # obtengo las parroquias de un canton
    return render(request, 'listado_parroquias.html', parroquia ,context_instance=RequestContext(request))

def cantpob(request):  
    

    id_cantpob= Cantpob.objects.all();

    cantpob={"id_cantpob":id_cantpob}
    # obtengo las parroquias de un canton
    return render(request, 'listado_parroquias.html', cantpob ,context_instance=RequestContext(request))    


def discapacidad(request):  
    

    id_discapacidad= Discapacidad.objects.all();

    discapacidad={"id_discapacidad":id_discapacidad}
    # obtengo las parroquias de un canton
    return render(request, 'mapas.html', discapacidad ,context_instance=RequestContext(request))        


def parrodis(request):  
    

    id_parrodis= Parrodis.objects.all();

    parrodis={"id_parrodis":id_parrodis}
    # obtengo las parroquias de un canton
    return render(request, 'listado_parroquias.html', parrodis ,context_instance=RequestContext(request))       


def poblacion5Anios(request):  
    

    id_poblacion5Anios= Poblacion5Anios.objects.all();

    poblacion5Anios={"id_poblacion5Anios":id_poblacion5Anios}
    # obtengo las parroquias de un canton
    return render(request, 'listado_parroquias.html', poblacion5Anios ,context_instance=RequestContext(request))   


def tipo(request):  
    

    id_tipo= Tipo.objects.all();

    tipo={"id_tipo":id_tipo}
    # obtengo las parroquias de un canton
    return render(request, 'listado_parroquias.html', tipo ,context_instance=RequestContext(request))          

def discapacidadesPastel(request):

    id_provincia= Provincia.objects.all()
    id_tipo= Tipo.objects.all()
    si=0
    no=0
    tipo={"id_provincia":id_provincia} 
    if request.method == "POST":
        valor1=request.POST["selProvDis"]
        valor2=request.POST["selTipoDis"]
        discapacidadesPastel=Parrodis.objects.filter(id_parroquia__id_canton__id_provincia__pk=int(valor1),id_discapacidad__id_tipo__pk=int(valor2))
        
        for d in discapacidadesPastel: 
            si=d.id_discapacidad.si
            no=d.id_discapacidad.no

    tipo={"id_provincia":id_provincia,"id_tipo":id_tipo,"si":si,"no":no}
    # obtengo las parroquias de un canton
    return render(request, 'discapacidadesPastel.html', tipo ,context_instance=RequestContext(request))

def discapacidadesBarras(request):

    id_provincia= Provincia.objects.all()
    id_tipo= Tipo.objects.all()
    si=0
    no=0
    tipo={"id_provincia":id_provincia} 
    if request.method == "POST":
        valor1=request.POST["selProvDis"]
        valor2=request.POST["selTipoDis"]
        discapacidadesBarras=Parrodis.objects.filter(id_parroquia__id_canton__id_provincia__pk=int(valor1),id_discapacidad__id_tipo__pk=int(valor2))
        
        for d in discapacidadesBarras: 
            si=d.id_discapacidad.si
            no=d.id_discapacidad.no


    tipo={"id_provincia":id_provincia,"id_tipo":id_tipo,"si":si,"no":no}
    # obtengo las parroquias de un canton
    return render(request, 'discapacidadesBarras.html', tipo ,context_instance=RequestContext(request))                