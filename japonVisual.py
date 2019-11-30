# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from tkinter import *
from tkinter.ttk import *
from networkx import *
from heapq import *
import matplotlib.pyplot as plt
import csv
#Debugger
#import pdb; pdb.set_trace()

#Diccionario (nombres estaciones - f, g, puntero, posH)        
diccNodos = {"Shinagawa": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 0} ,"Osaki": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 1} ,
            "Gotanda": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 2} ,"Meguro": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 3} ,
            "Ebisu": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 4} ,"Shibuya": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 5} ,
            "Harajuku": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 6} ,"Yoyogi": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 7} ,
            "Sobu Yoyogi": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 7} ,"Yamanote Yoyogi": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 7} , 
            "Shinjuku": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 8} ,"Sobu Shinjuku": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 8} , 
            "Chuo Shinjuku": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 8} , "Yamanote Shinjuku": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 8} ,
            "Shin-Okubo": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 9} ,"Takadanobaba": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 10} ,
            "Mejiro": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 11} ,"Ikebukuro": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 12} ,
            "Otsuka": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 13} ,"Sugamo": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 14} ,
            "Komagome": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 15} ,"Tabata": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 16} ,
            "Nishi-Nippori": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 17} ,"Nippori": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 18} ,
            "Uguisudani": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 19} ,"Ueno": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 20} ,
            "Okachimachi": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 21} ,"Akihabara": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 22} , 
            "Yamanote Akihabara": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 22} , "Sobu Akihabara": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 22} ,
            "Kanda": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 23} ,"Tokyo": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 24} ,
            "Yamanote Tokyo": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 24} ,"Chuo Tokyo": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 24} ,
            "Yurakucho": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 25} ,"Shimbashi": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 26} ,
            "Hamamatsucho": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 27} ,"Tamachi": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 28} ,
            "Ochanomizu": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 29} , "Sobu Ochanomizu": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 29} , 
            "Chuo Ochanomizu": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 29} ,"Suidobashi": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 30} ,
            "Iidabashi": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 31} ,"Ichigaya": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 32} ,
            "Yotsuya": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 33} ,"Shinanomachi": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 34} ,
            "Sendagaya": {'f': -1, 'g': -1, 'puntero': -1, 'posH': 35}}

#Grafo ()
G = Graph()
posNodos={
"Shinagawa":(327,18),
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

G.add_edges_from([("Yamanote Shinjuku","Shin-Okubo", {'color':'green', 'weight':1.3}),
                 ("Shin-Okubo","Takadanobaba", {'color':'green', 'weight':1.4}),
                 ("Takadanobaba", "Mejiro", {'color':'green', 'weight':0.9}), 
                 ("Mejiro", "Ikebukuro", {'color':'green', 'weight':1.2}),
                 ("Ikebukuro", "Otsuka", {'color':'green', 'weight':1.8}),
                 ("Otsuka", "Sugamo", {'color':'green', 'weight':0.9}),
                 ("Sugamo", "Komagome", {'color':'green', 'weight':0.7}),
                 ("Komagome", "Tabata", {'color':'green', 'weight':1.6}),
                 ("Tabata", "Nishi-Nippori", {'color':'green', 'weight':0.8}),
                 ("Nishi-Nippori", "Nippori", {'color':'green', 'weight':0.5}),
                 ("Nippori", "Uguisudani", {'color':'green', 'weight':1.1}),
                 ("Uguisudani", "Ueno", {'color':'green', 'weight':1.1}),
                 ("Ueno", "Okachimachi", {'color':'green', 'weight':0.6}),
                 ("Okachimachi", "Yamanote Akihabara", {'color':'green', 'weight':1.0}),
                 ("Yamanote Akihabara", "Akihabara", {'color':'grey', 'weight':0.0}),
                 ("Yamanote Akihabara", "Kanda", {'color':'green', 'weight':0.7}),
                 ("Kanda", "Yamanote Tokyo", {'color':'green', 'weight':1.3}),
                 ("Yamanote Tokyo", "Tokyo", {'color':'blue', 'weight':0.0}),
                 ("Yamanote Tokyo", "Yurakucho", {'color':'green', 'weight':0.8}),
                 ("Yurakucho", "Shimbashi", {'color':'green', 'weight':1.1}),
                 ("Shimbashi", "Hamamatsucho", {'color':'green', 'weight':1.2}),
                 ("Hamamatsucho", "Tamachi", {'color':'green', 'weight':1.5}),
                 ("Tamachi", "Shinagawa", {'color':'green', 'weight':2.2}), 
                 ("Shinagawa", "Osaki", {'color':'green', 'weight':2.0}),
                 ("Osaki", "Gotanda", {'color':'green', 'weight':0.9}),
                 ("Gotanda", "Meguro", {'color':'green', 'weight':1.2}),
                 ("Meguro", "Ebisu", {'color':'green', 'weight':1.5}),
                 ("Ebisu", "Shibuya", {'color':'green', 'weight':1.6}),
                 ("Shibuya", "Harajuku", {'color':'green', 'weight':1.2}),
                 ("Harajuku", "Yamanote Yoyogi", {'color':'green', 'weight':1.5}),
                 ("Yamanote Yoyogi", "Yoyogi", {'color':'blue', 'weight':0.0}),
                 ("Yamanote Yoyogi", "Yamanote Shinjuku", {'color':'green', 'weight':0.7}),
                 ("Yamanote Shinjuku", "Shinjuku", {'color':'blue', 'weight':0.0}),
                 ("Shinjuku", "Chuo Shinjuku", {'color':'blue', 'weight':0.0}),
                 ("Chuo Shinjuku", "Chuo Ochanomizu", {'color':'red', 'weight':7.7}),
                 ("Chuo Ochanomizu", "Ochanomizu", {'color':'blue', 'weight':0.0}),
                 ("Chuo Ochanomizu", "Chuo Tokyo", {'color':'red', 'weight':2.6}),
                 ("Chuo Tokyo", "Tokyo", {'color':'blue', 'weight':0.0}),
                 ("Shinjuku", "Sobu Shinjuku", {'color':'blue', 'weight':0.0}),
                 ("Sobu Shinjuku", "Sobu Yoyogi", {'color':'yellow', 'weight':0.7}),
                 ("Sobu Yoyogi", "Yoyogi", {'color':'grey', 'weight':0.0}),
                 ("Sobu Yoyogi", "Sendagaya", {'color':'yellow', 'weight':1.0}),
                 ("Sendagaya", "Shinanomachi", {'color':'yellow', 'weight':0.7}),
                 ("Shinanomachi", "Yotsuya", {'color':'yellow', 'weight':1.3}),
                 ("Yotsuya", "Ichigaya", {'color':'yellow', 'weight':0.8}),
                 ("Ichigaya", "Iidabashi", {'color':'yellow', 'weight':1.5}),
                 ("Iidabashi", "Suidobashi", {'color':'yellow', 'weight':0.9}),
                 ("Suidobashi", "Sobu Ochanomizu", {'color':'yellow', 'weight':0.8}),
                 ("Sobu Ochanomizu", "Ochanomizu", {'color':'blue', 'weight':0.0}),
                 ("Sobu Ochanomizu", "Sobu Akihabara", {'color':'yellow', 'weight':0.9}),
                 ("Sobu Akihabara", "Akihabara", {'color':'blue', 'weight':0.0}),
                 ("Yamanote Yoyogi", "Sobu Yoyogi", {'color' :'grey', 'weight':0.2}),
                 ("Yamanote Shinjuku", "Chuo Shinjuku", {'color':'grey', 'weight':0.2}),
                 ("Yamanote Akihabara", "Sobu Akihabara", {'color':'grey', 'weight':0.2})
                 ])

colorLinea={'green': 'Yamanote', 'red': 'Chuo', 'yellow': 'Sobu', 'grey': 'Interchange','blue': 'Simbolic'}

def algoritmoA_Estrella(origenNombre, destinoNombre,G) :
    origen = diccNodos[origenNombre]
    destino = diccNodos[destinoNombre]
    #PriorityQueue de duplas (f , nombre)
    listaAbierta = []
    #Lista
    listaCerrada = []
    #Heuristica
    h = [float(num) for num in cogerLinea(diccNodos[destinoNombre]['posH'])]
         
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
                g_nodoSiguiente = diccNodos[nodoPrometedor]['g'] + G.edges[nodoPrometedor, nodoSiguiente]['weight']
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
        return calcularRuta(origenNombre, destinoNombre)
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
        camino = algoritmoA_Estrella(origenNombre, destinoNombre, Gcopia.copy())
        linea = None
        longCamino = len(camino)
        for i in range(longCamino):
            if i == 0:
                padre=treeResultado.insert('','end',text=camino[i])
            elif i==longCamino-1:
                treeResultado.insert('','end',text=camino[i])
            else:
                if linea==None or colorLinea[Gcopia[camino[i-1]][camino[i]]['color']]!=linea:
                    if colorLinea[Gcopia[camino[i-1]][camino[i]]['color']] == 'Interchange':
                        linea=colorLinea[Gcopia[camino[i]][camino[i+1]]['color']]
                    else:
                         linea=colorLinea[Gcopia[camino[i-1]][camino[i]]['color']]
                    if i ==1:
                        treeResultado.insert(padre,'end',text=camino[i])
                    else:
                        padre = treeResultado.insert('','end',text=camino[i])
                    treeResultado.set(padre,'linea',linea)
                    #treeResultado.item(padre,tags=('Yamanote'))
                else: 
                    treeResultado.insert(padre,'end',text=camino[i])

def pintarGraph():
    global camino
    #top = Toplevel()
    #top.title('Ruta en el Mapa')
    #topFrame= Frame(top)
    #topFrame.pack()
    #topFrame.config(width=600,height = 600)
    f = plt.figure(figsize=(18,15),dpi=100,num='Ruta en el Mapa')
    thismanager = plt.get_current_fig_manager()
    #Icon made by Freepik from www.flaticon.com
    thismanager.window.wm_iconbitmap("konoha.ico")
    a = f.add_subplot(111)
    plt.axis('off')
    
    Gcopia = G.copy()
    eliminarNodosAux(Gcopia)
    nodes= Gcopia.nodes()
    edges = Gcopia.edges()
    L = ['Shinjuku', 'Akihabara', 'Tokyo', 'Ochanomizu' , 'Yoyogi']
    caminoNodos = [parada for parada in camino if parada not in L]
    caminoEdges = [(caminoNodos[i],caminoNodos[i+1]) for i in range(len(caminoNodos)-1)]
    colorsE = [G[u][v]['color']for u,v in edges]
    weightsE = [4 + 2.2/(G[u][v]['weight']) for u,v in edges]
    nx.draw_networkx(Gcopia, posNodos,node_color='grey',node_size=200,width =weightsE,
                     alpha=0.8, with_labels=True, font_weight='bold', edge_color=colorsE)
    
    nx.draw_networkx_edges(Gcopia, posNodos,
                       edgelist=caminoEdges,
                       width=[4 + 2.2/Gcopia[caminoNodos[i]][caminoNodos[i+1]]['weight'] for i in range(len(caminoNodos)-1)],
                       edge_color='b',alpha=0.7)

    xlim=a.get_xlim()
    ylim=a.get_ylim()
    plt.show()
    #canvas = FigureCanvasTkAgg(f,master= frame)
    #canvas.show()
    #canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=True)
    
    
root = Tk()
root.title("Metro Japón")
root.resizable(0, 0)
#Icon made by Freepik from www.flaticon.com
#https://www.flaticon.com/free-icon/japan_203070?term=japan%20flag&page=1&position=3
root.iconbitmap('japan.ico')

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


camino = None

botonCalcular  = Button (frame, command=calcularResumenCamino, text = "Calcular ruta")
botonCalcular.grid(row=4, column=0 ,padx=5, pady=5)

botonPintarGrafo=Button (frame,command = pintarGraph,text = "Dibujar ruta",state=DISABLED)
botonPintarGrafo.grid(row=5, column=0 ,padx=5, pady=5)

labelResultado = Label(frame,text = "Resultado:")
labelResultado.grid(row=0, column=1, sticky=W ,padx=5, pady=5)

treeResultado = Treeview(frame)


treeResultado.grid (row=1, column=1, rowspan=5, sticky=W ,padx=5, pady=5)
treeResultado.config(columns=("linea"))
treeResultado.column('linea',width=150,anchor='center')
treeResultado.heading('#0',text='Estación')
treeResultado.heading('linea',text='Linea')

treeResultado.tag_configure('Chuo', background='red')
treeResultado.tag_configure('Yamanote', background='green')
treeResultado.tag_configure('Sobu', background='yellow')

ysb = Scrollbar(frame,orient=VERTICAL, command= treeResultado.yview)
treeResultado['yscroll'] = ysb.set 
ysb.grid(row=1, column=2, rowspan=5, sticky='nsew')


root.mainloop()
   
    
    
    
    
