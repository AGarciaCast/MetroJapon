#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from networkx import *
from heapq import *
import csv
#Debugger
#import pdb; pdb.set_trace()

#Diccionario (nombres estaciones - f, g, puntero, posH)        
diccNodos = {"Shinagawa": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 0},
            "Osaki": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 1},
            "Gotanda": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 2},
            "Meguro": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 3},
            "Ebisu": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 4},
            "Shibuya": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 5},
            "Harajuku": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 6},
            "Yoyogi": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 7},
            "Sobu Yoyogi": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 7},
            "Yamanote Yoyogi": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 7}, 
            "Shinjuku": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 8},
            "Sobu Shinjuku": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 8},
            "Chuo Shinjuku": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 8},
            "Yamanote Shinjuku": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 8},
            "Shin-Okubo": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 9},
            "Takadanobaba": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 10},
            "Mejiro": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 11},
            "Ikebukuro": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 12},
            "Otsuka": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 13},
            "Sugamo": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 14},
            "Komagome": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 15},
            "Tabata": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 16},
            "Nishi-Nippori": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 17},
            "Nippori": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 18},
            "Uguisudani": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 19},
            "Ueno": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 20},
            "Okachimachi": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 21},
            "Akihabara": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 22}, 
            "Yamanote Akihabara": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 22},
            "Sobu Akihabara": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 22},
            "Kanda": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 23},
            "Tokyo": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 24},
            "Yamanote Tokyo": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 24},
            "Chuo Tokyo": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 24},
            "Yurakucho": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 25},
            "Shimbashi": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 26},
            "Hamamatsucho": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 27},
            "Tamachi": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 28},
            "Ochanomizu": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 29},
            "Sobu Ochanomizu": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 29}, 
            "Chuo Ochanomizu": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 29},
            "Suidobashi": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 30},
            "Iidabashi": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 31},
            "Ichigaya": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 32},
            "Yotsuya": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 33},
            "Shinanomachi": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 34},
            "Sendagaya": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 35}
            }

posNodos={"Shinagawa":(327,18),
          "Osaki":(260,9),
          "Gotanda":(215,9),
          "Meguro":(175,9),
          "Ebisu":(120,36),
          "Shibuya":(120,97),
          "Harajuku":(120,150),
          "Yoyogi":(120,230),
          "Sobu Yoyogi":(70,230),
          "Yamanote Yoyogi":(120,230),
          "Shinjuku":(120,273),
          "Sobu Shinjuku":(70,273),
          "Chuo Shinjuku":(92,315),
          "Yamanote Shinjuku":(120,273),
          "Shin-Okubo":(120,360),
          "Takadanobaba":(125,406),
          "Mejiro":(166,467),
          "Ikebukuro":(233,490),
          "Otsuka":(311,488),
          "Sugamo":(350,488),
          "Komagome":(387,488),
          "Tabata":(436,470),
          "Nishi-Nippori":(458,446),
          "Nippori":(465,410),
          "Uguisudani":(465,380),
          "Ueno":(465,350),
          "Okachimachi":(465,317),
          "Akihabara":(465,286),
          "Yamanote Akihabara":(465,286),
          "Sobu Akihabara":(410,286),
          "Kanda":(465,238),
          "Tokyo":(465,192),
          "Yamanote Tokyo":(465,192),
          "Chuo Tokyo":(415,192),
          "Yurakucho":(460,150),
          "Shimbashi":(433,123),
          "Hamamatsucho":(400,91),
          "Tamachi":(365,56),
          "Ochanomizu":(335,309),
          "Sobu Ochanomizu":(314,286),
          "Chuo Ochanomizu":(335,315),
          "Suidobashi":(283,264),
          "Iidabashi":(263,244),
          "Ichigaya":(243,224),
          "Yotsuya":(223,204),
          "Shinanomachi":(195,180),
          "Sendagaya":(146,180)
          }

#Grafo ()
G = Graph()


G.add_edges_from([("Yamanote Shinjuku","Shin-Okubo", {'color':'green', 'weight':1.3,'tiempo':0}),
                 ("Shin-Okubo","Takadanobaba", {'color':'green', 'weight':1.4,'tiempo':0}),
                 ("Takadanobaba", "Mejiro", {'color':'green', 'weight':0.9,'tiempo':0}), 
                 ("Mejiro", "Ikebukuro", {'color':'green', 'weight':1.2,'tiempo':0}),
                 ("Ikebukuro", "Otsuka", {'color':'green', 'weight':1.8,'tiempo':0}),
                 ("Otsuka", "Sugamo", {'color':'green', 'weight':0.9,'tiempo':0}),
                 ("Sugamo", "Komagome", {'color':'green', 'weight':0.7,'tiempo':0}),
                 ("Komagome", "Tabata", {'color':'green', 'weight':1.6,'tiempo':0}),
                 ("Tabata", "Nishi-Nippori", {'color':'green', 'weight':0.8,'tiempo':0}),
                 ("Nishi-Nippori", "Nippori", {'color':'green', 'weight':0.5,'tiempo':0}),
                 ("Nippori", "Uguisudani", {'color':'green', 'weight':1.1,'tiempo':0}),
                 ("Uguisudani", "Ueno", {'color':'green', 'weight':1.1,'tiempo':0}),
                 ("Ueno", "Okachimachi", {'color':'green', 'weight':0.6,'tiempo':0}),
                 ("Okachimachi", "Yamanote Akihabara", {'color':'green', 'weight':1.0,'tiempo':0}),
                 ("Yamanote Akihabara", "Akihabara", {'color':'green', 'weight':0.0,'tiempo':0}),
                 ("Yamanote Akihabara", "Kanda", {'color':'green', 'weight':0.7,'tiempo':0}),
                 ("Kanda", "Yamanote Tokyo", {'color':'green', 'weight':1.3,'tiempo':0}),
                 ("Yamanote Tokyo", "Tokyo", {'color':'green', 'weight':0.0,'tiempo':0}),
                 ("Yamanote Tokyo", "Yurakucho", {'color':'green', 'weight':0.8,'tiempo':0}),
                 ("Yurakucho", "Shimbashi", {'color':'green', 'weight':1.1,'tiempo':0}),
                 ("Shimbashi", "Hamamatsucho", {'color':'green', 'weight':1.2,'tiempo':0}),
                 ("Hamamatsucho", "Tamachi", {'color':'green', 'weight':1.5,'tiempo':0}),
                 ("Tamachi", "Shinagawa", {'color':'green', 'weight':2.2,'tiempo':0}), 
                 ("Shinagawa", "Osaki", {'color':'green', 'weight':2.0,'tiempo':0}),
                 ("Osaki", "Gotanda", {'color':'green', 'weight':0.9,'tiempo':0}),
                 ("Gotanda", "Meguro", {'color':'green', 'weight':1.2,'tiempo':0}),
                 ("Meguro", "Ebisu", {'color':'green', 'weight':1.5,'tiempo':0}),
                 ("Ebisu", "Shibuya", {'color':'green', 'weight':1.6,'tiempo':0}),
                 ("Shibuya", "Harajuku", {'color':'green', 'weight':1.2,'tiempo':0}),
                 ("Harajuku", "Yamanote Yoyogi", {'color':'green', 'weight':1.5,'tiempo':0}),
                 ("Yamanote Yoyogi", "Yoyogi", {'color':'green', 'weight':0.0,'tiempo':0}),
                 ("Yamanote Yoyogi", "Yamanote Shinjuku", {'color':'green', 'weight':0.7,'tiempo':0}),
                 ("Yamanote Shinjuku", "Shinjuku", {'color':'green', 'weight':0.0,'tiempo':0}),
                 ("Shinjuku", "Chuo Shinjuku", {'color':'red', 'weight':0.0,'tiempo':0}),
                 ("Chuo Shinjuku", "Chuo Ochanomizu", {'color':'red', 'weight':7.7,'tiempo':0}),
                 ("Chuo Ochanomizu", "Ochanomizu", {'color':'red', 'weight':0.0,'tiempo':0}),
                 ("Chuo Ochanomizu", "Chuo Tokyo", {'color':'red', 'weight':2.6,'tiempo':0}),
                 ("Chuo Tokyo", "Tokyo", {'color':'red', 'weight':0.0,'tiempo':0}),
                 ("Shinjuku", "Sobu Shinjuku", {'color':'yellow', 'weight':0.0,'tiempo':0}),
                 ("Sobu Shinjuku", "Sobu Yoyogi", {'color':'yellow', 'weight':0.7,'tiempo':0}),
                 ("Sobu Yoyogi", "Yoyogi", {'color':'yellow', 'weight':0.0,'tiempo':0}),
                 ("Sobu Yoyogi", "Sendagaya", {'color':'yellow', 'weight':1.0,'tiempo':0}),
                 ("Sendagaya", "Shinanomachi", {'color':'yellow', 'weight':0.7,'tiempo':0}),
                 ("Shinanomachi", "Yotsuya", {'color':'yellow', 'weight':1.3,'tiempo':0}),
                 ("Yotsuya", "Ichigaya", {'color':'yellow', 'weight':0.8,'tiempo':0}),
                 ("Ichigaya", "Iidabashi", {'color':'yellow', 'weight':1.5,'tiempo':0}),
                 ("Iidabashi", "Suidobashi", {'color':'yellow', 'weight':0.9,'tiempo':0}),
                 ("Suidobashi", "Sobu Ochanomizu", {'color':'yellow', 'weight':0.8,'tiempo':0}),
                 ("Sobu Ochanomizu", "Ochanomizu", {'color':'yellow', 'weight':0.0,'tiempo':0}),
                 ("Sobu Ochanomizu", "Sobu Akihabara", {'color':'yellow', 'weight':0.9,'tiempo':0}),
                 ("Sobu Akihabara", "Akihabara", {'color':'yellow', 'weight':0.0,'tiempo':0}),
                 ("Yamanote Yoyogi", "Sobu Yoyogi", {'color' :'grey', 'weight':0.08,'tiempo':0}),
                 ("Yamanote Shinjuku", "Chuo Shinjuku", {'color':'grey', 'weight':0.08,'tiempo':0}),
                 ("Yamanote Akihabara", "Sobu Akihabara", {'color':'grey', 'weight':0.08,'tiempo':0}), 
                 ("Chuo Ochanomizu", "Sobu Ochanomizu", {'color':'grey', 'weight':0.02,'tiempo':0}), 
                 ("Yamanote Shinjuku", "Sobu Shinjuku", {'color':'grey', 'weight':0.14,'tiempo':0}), 
                 ("Yamanote Tokyo", "Chuo Tokyo", {'color':'grey', 'weight':0.25,'tiempo':0}), 
                 ("Sobu Shinjuku", "Chuo Shinjuku", {'color':'grey', 'weight':0.18,'tiempo':0})
                 ] )


infoLinea={'green': {'nombre':'Yamanote','velocidad':90},
           'red': {'nombre':'Chuo','velocidad':95}, 
           'yellow':{ 'nombre':'Sobu','velocidad':100},
           'grey': {'nombre':'Interchange','velocidad':5}
           }


for u,v in G.edges():
    peso =G[u][v]['weight']
    color = G[u][v]['color']
    tiempo = 0
    if peso!=0:
        tiempo = peso/infoLinea[color]['velocidad']*60
        if color=='grey':
            if color.split()[0]=='Yamanote':
                tiempo += 2.5
            else:
                tiempo += 3.0
        else:
            tiempo += 1.5
        G[u][v]['tiempo']=tiempo
   
            

def algoritmoA_Estrella(origenNombre, destinoNombre,G,transbordo) :
    origen = diccNodos[origenNombre]
    destino = diccNodos[destinoNombre]
    #PriorityQueue de duplas (f , nombre)
    listaAbierta = []
    #Lista
    listaCerrada = []
    #Heuristica en minutos
    h = [(float(num)/100) * 60 for num in cogerLinea(diccNodos[destinoNombre]['posH'])]
         
    #Inicializar el nodo origen  
    origen['g'] = 0
    origen['f'] = origen['g'] + h[origen['posH']]
    heappush(listaAbierta, (origen['f'], origenNombre))
    
    hemosLlegado = False 
    
    while (not hemosLlegado) :

        nodoPrometedor = heappop(listaAbierta)[1]
        listaCerrada.append(nodoPrometedor)
     
        if (nodoPrometedor == destinoNombre) :
            hemosLlegado = True
        else :
            for nodoSiguiente in list(G.adj[nodoPrometedor]):
                #Se calculan f y g provisionales pero todavia no se guardan
                g_nodoSiguiente = diccNodos[nodoPrometedor]['g'] + G.edges[nodoPrometedor, nodoSiguiente]['tiempo']
                #Penalizacion por transbordo
                if  G.edges[nodoPrometedor, nodoSiguiente]['color'] == 'grey':
                    g_nodoSiguiente += transbordo*100
                f_nodoSiguiente = g_nodoSiguiente + h[diccNodos[nodoSiguiente]['posH']] 
                G.remove_edge(nodoPrometedor, nodoSiguiente)
                
                #Si hay un elemento con nodoSiguiente en listaAbierta
                #(aunque no necesariamente con la f que se acaba de calcular)
                if (estaEn(listaAbierta, nodoSiguiente, 1) or (nodoSiguiente in listaCerrada)
                    and f_nodoSiguiente < diccNodos[nodoSiguiente]['f']) :
                    #Si mejora el camino, se guardan los nuevos f y g, 
                    #se actualizan el puntero y f en la listaAbierta
                    guardarValores(nodoSiguiente, g_nodoSiguiente, f_nodoSiguiente, nodoPrometedor)
                    actualizarValor(listaAbierta, nodoSiguiente, diccNodos[nodoSiguiente]['f'])
                #if (nodoSiguiente in listaCerrada) :
                    #TODO??
                if (not estaEn(listaAbierta, nodoSiguiente, 1) and (nodoSiguiente not in listaCerrada)) :
                    #Si no se habia explorado el nodo, se guardan f, g, puntero 
                    #y se introduce en la listaAbierta
                    guardarValores(nodoSiguiente, g_nodoSiguiente, f_nodoSiguiente, nodoPrometedor)
                    heappush(listaAbierta, (diccNodos[nodoSiguiente]['f'], nodoSiguiente))
                    
    if (hemosLlegado) :
        return calcularRuta(origenNombre, destinoNombre), diccNodos[destinoNombre]['f']
    else :
        print('Error')
                   

def guardarValores(nodo, valor_g, valor_f, nodoAnterior) :
    diccNodos[nodo]['g'] = valor_g
    diccNodos[nodo]['f'] = valor_f
    diccNodos[nodo]['puntero'] = nodoAnterior
    
#Mira si hay una dupla en la lista de duplas cuya coordenada n-esima sea elem
def estaEn(listaDuplas, elem, n):
    return len([dupla[n] for dupla in listaDuplas if dupla[n] == elem]) > 0
            
#Actualiza un valor en un heap
def actualizarValor(heap, nodo, nuevoValor) :
    #Busca y elimina el antiguo
    elemento = [dupla for dupla in heap if dupla[1] == nodo][0]
    heap.remove(elemento)
    #Reconvierte en heap
    heapify(heap)
    #Añade el elemento con el nuevo valor
    heappush(heap, (nuevoValor, nodo))
    
#Devuelve una lista con los nombres de los nodos del camino optimo en orden 
def calcularRuta(origenNombre, destinoNombre) :
    camino = [destinoNombre]
    if (destinoNombre == origenNombre): return camino
    anterior = diccNodos[destinoNombre]['puntero']
    while (anterior != origenNombre) :
        camino.append(anterior)
        anterior = diccNodos[anterior]['puntero']
    camino.append(origenNombre)
    camino.reverse()
    return camino
          
#Toma la linea "fila"+2 del csv
def cogerLinea(fila):
    with open('Datos/heuristicaMetroJapon.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for i in range(fila+1):
            next(reader)
        return next(reader)
    
def eliminarNodosAux(G,origenNombre=None, destinoNombre=None):
    L = ['Shinjuku', 'Akihabara', 'Tokyo', 'Ochanomizu' , 'Yoyogi']
    for nodo in L: 
        if (nodo != origenNombre and nodo != destinoNombre) :
           G.remove_node(nodo)

click_counter=0

def calcularResumenCamino():
    if(seleccionOrigen.current() !=-1 and seleccionDestino.current()!=-1):
        #Habilita el boton de dibujar
        if str(botonPintarGrafo['state']) == 'disabled':
            botonPintarGrafo['state'] = 'normal'
        global camino
        treeResultado.delete(*treeResultado.get_children())
        origenNombre = seleccionOrigen.get()
        destinoNombre = seleccionDestino.get()
        Gcopia = G.copy()
        eliminarNodosAux(Gcopia, origenNombre, destinoNombre)
        camino,tiempoCamino = algoritmoA_Estrella(origenNombre, destinoNombre, Gcopia.copy(),estadoTransbordo.get())
        tiempoTotal = (1-estadoTransbordo.get())*tiempoCamino
        linea = None
        longCamino = len(camino)
        for i in range(longCamino):
            if i == 0:
                padre=treeResultado.insert('','end',text=camino[i])
                nuevo = padre
            else:
                if linea==None or infoLinea[Gcopia[camino[i-1]][camino[i]]['color']]['nombre']!=linea:
                    if infoLinea[Gcopia[camino[i-1]][camino[i]]['color']]['nombre'] == 'Interchange':
                        linea=infoLinea[Gcopia[camino[i]][camino[i+1]]['color']]['nombre']
                    else:
                         linea=infoLinea[Gcopia[camino[i-1]][camino[i]]['color']]['nombre']
                         
                    if i ==1:
                         if i == longCamino-1:
                             nuevo = treeResultado.insert('','end',text=camino[i])
                         else:
                             nuevo =treeResultado.insert(padre,'end',text=camino[i])
                    else:
                        padre = treeResultado.insert('','end',text=camino[i])
                        nuevo = padre
                    treeResultado.set(padre,'linea',linea)
                else: 
                    if i == longCamino-1:
                         nuevo = treeResultado.insert('','end',text=camino[i])
                    else :
                        nuevo = treeResultado.insert(padre,'end',text=camino[i])
                
            if i==1:
                treeResultado.set(nuevo, 'distancia',str(Gcopia[camino[i-1]][camino[i]]['weight']))
                treeResultado.item(padre,tags=(linea,'IO'))
                
                if estadoTransbordo.get()==1:
                    tiempoTotal += Gcopia[camino[i-1]][camino[i]]['tiempo']
                    
                if i == longCamino-1:
                    treeResultado.item(nuevo,tags=(linea,'IO'))
                else:
                    treeResultado.item(nuevo,tags=(linea))
                    
            elif i!=0:
                treeResultado.set(nuevo, 'distancia',
                                  round(float(treeResultado.item(ultimo)['values'][1]) + Gcopia[camino[i-1]][camino[i]]['weight'],1))
                
                if estadoTransbordo.get()==1:
                    tiempoTotal += Gcopia[camino[i-1]][camino[i]]['tiempo']
                    
                if i == longCamino-1:
                    treeResultado.item(nuevo,tags=(linea,'IO'))
                else:
                    treeResultado.item(nuevo,tags=(linea))
           
            ultimo = nuevo
            
        labelResultado['text']='Resultado: ' + str(round(tiempoTotal,2)) +' min'       
    else:
        global click_counter
        click_counter+=1
        if click_counter<=10:
            messagebox.showinfo('Calular Ruta','Tienes que selecionar previamente el origen y el destino.') 
        else:
             messagebox.showinfo('経路計算をする','以前は,発信元と宛先を選択する必要があります。')
                      
                     
colorPastel={'red':'#f17c73','green':'#6adf88','yellow':'#f1f073','blue':'#4751cc','grey':'#ccccc7'}

def pintarGraph():
    global camino
    plt.close()
    f = plt.figure(figsize=(18,15),dpi=100,num='Ruta en el Mapa')
    thismanager = plt.get_current_fig_manager()
    thismanager.window.wm_iconbitmap("konoha.ico")
    thismanager.window.state('zoomed')
    a = f.add_subplot(111)
    plt.axis('off')
    
    Gcopia = G.copy()
    eliminarNodosAux(Gcopia)
    nodes= Gcopia.nodes()
    edges = Gcopia.edges()
    L = ['Shinjuku', 'Akihabara', 'Tokyo', 'Ochanomizu' , 'Yoyogi']
    caminoNodos = [parada for parada in camino if parada not in L]
    caminoEdges = [(caminoNodos[i],caminoNodos[i+1]) for i in range(len(caminoNodos)-1)]
    colorsE = [colorPastel[G[u][v]['color']] for u,v in edges]
    weightsE = [min(4 + 2.2/(G[u][v]['weight']),16) for u,v in edges]
    nx.draw_networkx(Gcopia, posNodos,node_color='grey',node_size=200,width =weightsE,
                     with_labels=True, font_weight='bold', edge_color=colorsE)
    
    nx.draw_networkx_edges(Gcopia, posNodos,
                       edgelist=caminoEdges,
                       width=[min(4 + 2.2/Gcopia[caminoNodos[i]][caminoNodos[i+1]]['weight'],16) for i in range(len(caminoNodos)-1)],
                       edge_color=colorPastel['blue'],alpha=0.7)
    xlim=a.get_xlim()
    a.set_xlim([xlim[0],xlim[1]+10])
   
    
    leyendaRojo = mpatches.Patch(color=colorPastel['red'], label='Chuo Line')
    leyendaAmarillo = mpatches.Patch(color=colorPastel['yellow'], label='Sobu Line')
    leyendaVerde = mpatches.Patch(color=colorPastel['green'], label='Yamanote Line')
    leyendaGris = mpatches.Patch(color=colorPastel['grey'], label='Intercambio')
    leyendaAzul = mpatches.Patch(color=colorPastel['blue'], label='Trayecto óptimo')
    
    plt.legend(handles=[leyendaVerde,leyendaRojo,leyendaAmarillo,leyendaGris,leyendaAzul])
    
    plt.show()

def alertaMuchoTiempo():
    if estadoTransbordo.get() == 1:
        messagebox.showwarning('Advertencia','Al seleccionar esta opción el resultado puede tartar en calcularse más de lo normal.')
 
    
def finProg():
    plt.close()
    root.destroy()
def fixed_map(option):
    # Fix for setting text colour for Tkinter 8.6.9
    # From: https://core.tcl.tk/tk/info/509cafafae
    #
    # Returns the style map for 'option' with any styles starting with
    # ('!disabled', '!selected', ...) filtered out.
    
    # style.map() returns an empty list for missing options, so this
    # should be future-safe.
    return [elm for elm in style.map('Treeview', query_opt=option) if elm[:2] != ('!disabled', '!selected')]

root = Tk()
root.title("Metro Japón")
root.resizable(0, 0)
#Icon made by Freepik from www.flaticon.com
#https://www.flaticon.com/free-icon/japan_203070?term=japan%20flag&page=1&position=3
root.iconbitmap('japan.ico')
root.protocol('WM_DELETE_WINDOW', finProg)
frame= Frame(root)
frame.pack()
frame.config(width=600,height = 600)

labelOrigen = Label(frame, text = "Origen:")
labelOrigen.grid(row=0, column=0, sticky=W ,padx=5, pady=5)

seleccionOrigen = Combobox(frame, state="readonly")
seleccionOrigen.grid(row=1, column =0,padx=5, pady=5)
seleccionOrigen["values"] = ("Shinagawa","Osaki","Gotanda","Meguro","Ebisu","Shibuya","Harajuku","Yoyogi",
                            "Shinjuku","Shin-Okubo","Takadanobaba","Mejiro","Ikebukuro","Otsuka","Sugamo",
                            "Komagome","Tabata","Nishi-Nippori","Nippori","Uguisudani","Ueno","Okachimachi",
                            "Akihabara","Kanda","Tokyo","Yurakucho","Shimbashi","Hamamatsucho","Tamachi",
                            "Ochanomizu","Suidobashi","Iidabashi","Ichigaya","Yotsuya","Shinanomachi","Sendagaya")

labelDestino = Label(frame, text = "Destino:")
labelDestino.grid(row=2, column=0, sticky=W ,padx=5, pady=5)

seleccionDestino = Combobox(frame, state="readonly")
seleccionDestino.grid(row=3, column =0,padx=5, pady=5)
seleccionDestino["values"] = ("Shinagawa","Osaki","Gotanda","Meguro","Ebisu","Shibuya","Harajuku","Yoyogi",
                            "Shinjuku","Shin-Okubo","Takadanobaba","Mejiro","Ikebukuro","Otsuka","Sugamo",
                            "Komagome","Tabata","Nishi-Nippori","Nippori","Uguisudani","Ueno","Okachimachi",
                            "Akihabara","Kanda","Tokyo","Yurakucho","Shimbashi","Hamamatsucho","Tamachi",
                            "Ochanomizu","Suidobashi","Iidabashi","Ichigaya","Yotsuya","Shinanomachi","Sendagaya")

estadoTransbordo = IntVar()

opcionTransbordo= Checkbutton(frame, text = 'Mínino número de transbordos',
                              variable = estadoTransbordo,onvalue = 1, offvalue=0,command=alertaMuchoTiempo)

opcionTransbordo.grid(row=4, column =0,padx=5, pady=5)
camino = None

botonCalcular  = Button (frame, command=calcularResumenCamino, text = "Calcular ruta")
botonCalcular.grid(row=5, column=0 ,padx=5, pady=5)

botonPintarGrafo=Button (frame,command = pintarGraph,text = "Dibujar ruta",state=DISABLED)
botonPintarGrafo.grid(row=6, column=0 ,padx=5, pady=5)

labelResultado = Label(frame,text = "Resultado:")
labelResultado.grid(row=0, column=1, sticky=W ,padx=5, pady=5)

style = Style()
style.map('Treeview', foreground=fixed_map('foreground'), background=fixed_map('background'))
treeResultado = Treeview(frame,selectmode='none')
treeResultado.grid (row=1, column=1, rowspan=6, sticky=W ,padx=5, pady=7)
treeResultado.config(columns=("linea",'distancia'))
treeResultado.column('linea',width=130,anchor='center')
treeResultado.column('distancia',width=150,anchor='center')
treeResultado.heading('#0',text='Estación')
treeResultado.heading('linea',text='Linea')
treeResultado.heading('distancia',text='Distancia Recorrida (km)')

treeResultado.tag_configure('Chuo', background=colorPastel['red'])
treeResultado.tag_configure('Yamanote', background=colorPastel['green'])
treeResultado.tag_configure('Sobu', background=colorPastel['yellow'])
treeResultado.tag_configure('IO',foreground=colorPastel['blue'])

ysb = Scrollbar(frame,orient=VERTICAL, command= treeResultado.yview)
treeResultado['yscroll'] = ysb.set 
ysb.grid(row=1, column=2, rowspan=6, sticky='nsew')


root.mainloop()
   
    
    
    
    