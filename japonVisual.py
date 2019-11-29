# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.ttk import *
from networkx import *
from heapq import *
#Debugger
#import pdb; pdb.set_trace()
"""
root = Tk()
root.title("Metro Japón")

frame= Frame(root)
frame.pack()
frame.config(width=600,height = 600)

labelOrigen = Label(frame, text = "Origen:")
labelOrigen.grid(row=0, column=0, sticky=W ,padx=5, pady=5)

seleccionOrigen = Combobox(frame)
seleccionOrigen.grid(row=1, column =0,padx=5, pady=5)
seleccionOrigen["values"] = ("Shinagawa","Osaki","Gotanda","Meguro","Ebisu","Shibuya","Harajuku","Yoyogi",
                            "Shinjuku","Shin-Okubo","Takadanobaba","Mejiro","Ikebukuro","Otsuka","Sugamo",
                            "Komagome","Tabata","Nishi-Nippori","Nippori","Uguisudani","Ueno","Okachimachi",
                            "Akihabara","Kanda","Tokyo","Yurakucho","Shimbashi","Hamamatsucho","Tamachi",
                            "Ochanomizu","Suidobashi","Iidabashi","Ichigaya","Yotsuya","Shinanomachi","Sendagaya")

labelDestino = Label(frame, text = "Destino:")
labelDestino.grid(row=2, column=0, sticky=W ,padx=5, pady=5)

seleccionDestino = ttk.Combobox(frame)
seleccionDestino.grid(row=3, column =0,padx=5, pady=5)
seleccionDestino["values"] = ("Shinagawa","Osaki","Gotanda","Meguro","Ebisu","Shibuya","Harajuku","Yoyogi",
                            "Shinjuku","Shin-Okubo","Takadanobaba","Mejiro","Ikebukuro","Otsuka","Sugamo",
                            "Komagome","Tabata","Nishi-Nippori","Nippori","Uguisudani","Ueno","Okachimachi",
                            "Akihabara","Kanda","Tokyo","Yurakucho","Shimbashi","Hamamatsucho","Tamachi",
                            "Ochanomizu","Suidobashi","Iidabashi","Ichigaya","Yotsuya","Shinanomachi","Sendagaya")

botonCalcular  = Button (frame, text = "Calcular ruta")
botonCalcular.grid(row=4, column=0 ,padx=5, pady=5)


labelResultado = Label(frame, text = "Resultado:")
labelResultado.grid(row=0, column=1, sticky=W ,padx=5, pady=5)

 
root.mainloop()

"""

#Diccionario (nombres estaciones - numeros (de 0 hasta numNodos - 1 !!))
dicc = {"Shinagawa" : 0,"Osaki" : 1,"Gotanda" : 2,"Meguro" : 3,"Ebisu" : 4 ,"Shibuya" : 5,"Harajuku" : 6,"Yoyogi" : 7,
        "Sobu Yoyogi" : 8, "Yamanote Yoyogi" : 9, "Shinjuku" : 10,"Sobu Shinjuku" : 11, "Chuo Shinjuku" : 12, 
        "Yamanote Shinjuku" : 13, "Shin-Okubo" : 14, "Takadanobaba" : 15,"Mejiro" : 16, "Ikebukuro" : 17, 
        "Otsuka" : 18, "Sugamo" : 19, "Komagome" : 20, "Tabata" : 21, "Nishi-Nippori" : 22, "Nippori" : 23, 
        "Uguisudani" : 24, "Ueno" : 25, "Okachimachi" : 26, "Akihabara" : 27, "Yamanote Akihabara" : 28, 
        "Sobu Akihabara" : 29, "Kanda" : 30, "Tokyo" : 31, "Yamanote Tokyo" : 32, "Chuo Tokyo" : 33, "Yurakucho" : 34,
        "Shimbashi" : 35, "Hamamatsucho" : 36, "Tamachi" : 37, "Ochanomizu" : 38, "Sobu Ochanomizu" : 39, 
        "Chuo Ochanomizu" : 40, "Suidobashi" : 41, "Iidabashi" : 42, "Ichigaya" : 43, "Yotsuya" : 44,
        "Shinanomachi" : 45, "Sendagaya" : 46}
diccInv = {v: k for k, v in dicc.items()}


#Grafo ()
#TOCHECK
G = Graph()

'''listaNodos=["Shinagawa","Osaki","Gotanda","Meguro","Ebisu","Shibuya","Harajuku","Yoyogi","Sobu Yoyogi",
                            "Yamanote Yoyogi", "Shinjuku","Sobu Shinjuku", "Chuo Shinjuku", "Yamanote Shinjuku","Shin-Okubo",
                            "Takadanobaba","Mejiro","Ikebukuro","Otsuka","Sugamo",
                            "Komagome","Tabata","Nishi-Nippori","Nippori","Uguisudani","Ueno","Okachimachi",
                            "Akihabara", "Yamanote Akihabara", "Sobu Akihabara","Kanda","Tokyo", "Yamanote Tokyo","Chuo Tokyo" ,
                            "Yurakucho","Shimbashi","Hamamatsucho","Tamachi",
                            "Ochanomizu", "Sobu Ochanomizu", "Chuo Ochanomizu","Suidobashi","Iidabashi",
                            "Ichigaya","Yotsuya","Shinanomachi","Sendagaya"]

G.add_nodes_from(listaNodos)

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
                 ("Yamanote Tokyo", "Tokyo", {'color':'grey', 'weight':0.0}),
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
                 ("Yamanote Yoyogi", "Yoyogi", {'color':'grey', 'weight':0.0}),
                 ("Yamanote Yoyogi", "Yamanote Shinjuku", {'color':'green', 'weight':0.7}),
                 ("Yamanote Shinjuku", "Shinjuku", {'color':'grey', 'weight':0.0}),
                 ("Shinjuku", "Chuo Shinjuku", {'color':'grey', 'weight':0.0}),
                 ("Chuo Shinjuku", "Chuo Ochanomizu", {'color':'red', 'weight':7.7}),
                 ("Chuo Ochanomizu", "Ochanomizu", {'color':'grey', 'weight':0.0}),
                 ("Chuo Ochanomizu", "Chuo Tokyo", {'color':'red', 'weight':2.6}),
                 ("Chuo Tokyo", "Tokyo", {'color':'grey', 'weight':0.0}),
                 ("Shinjuku", "Sobu Shinjuku", {'color':'grey', 'weight':0.0}),
                 ("Sobu Shinjuku", "Sobu Yoyogi", {'color':'yellow', 'weight':0.7}),
                 ("Sobu Yoyogi", "Yoyogi", {'color':'grey', 'weight':0.0}),
                 ("Sobu Yoyogi", "Sendagaya", {'color':'yellow', 'weight':1.0}),
                 ("Sendagaya", "Shinanomachi", {'color':'yellow', 'weight':0.7}),
                 ("Shinanomachi", "Yotsuya", {'color':'yellow', 'weight':1.3}),
                 ("Yotsuya", "Ichigaya", {'color':'yellow', 'weight':0.8}),
                 ("Ichigaya", "Iidabashi", {'color':'yellow', 'weight':1.5}),
                 ("Iidabashi", "Suidobashi", {'color':'yellow', 'weight':0.9}),
                 ("Suidobashi", "Sobu Ochanomizu", {'color':'yellow', 'weight':0.8}),
                 ("Sobu Ochanomizu", "Ochanomizu", {'color':'grey', 'weight':0.0}),
                 ("Sobu Ochanomizu", "Sobu Akihabara", {'color':'yellow', 'weight':0.9}),
                 ("Sobu Akihabara", "Akihabara", {'color':'grey', 'weight':0.0}),
                 ("Yamanote Yoyogi", "Sobu Yoyogi", {'color' :'grey', 'weight':0.2}),
                 ("Yamanote Shinjuku", "Chuo Shinjuku", {'color':'grey', 'weight':0.2}),
                 ("Yamanote Akihabara", "Sobu Akihabara", {'color':'grey', 'weight':0.2})
                 ])'''

G.add_edges_from([(dicc["Yamanote Shinjuku"], dicc["Shin-Okubo"], {'color':'green', 'weight':1.3}),
                 (dicc["Shin-Okubo"], dicc["Takadanobaba"], {'color':'green', 'weight':1.4}),
                 (dicc["Takadanobaba"], dicc["Mejiro"], {'color':'green', 'weight':0.9}), 
                 (dicc["Mejiro"], dicc["Ikebukuro"], {'color':'green', 'weight':1.2}),
                 (dicc["Ikebukuro"], dicc["Otsuka"], {'color':'green', 'weight':1.8}),
                 (dicc["Otsuka"], dicc["Sugamo"], {'color':'green', 'weight':0.9}),
                 (dicc["Sugamo"], dicc["Komagome"], {'color':'green', 'weight':0.7}),
                 (dicc["Komagome"], dicc["Tabata"], {'color':'green', 'weight':1.6}),
                 (dicc["Tabata"], dicc["Nishi-Nippori"], {'color':'green', 'weight':0.8}),
                 (dicc["Nishi-Nippori"], dicc["Nippori"], {'color':'green', 'weight':0.5}),
                 (dicc["Nippori"], dicc["Uguisudani"], {'color':'green', 'weight':1.1}),
                 (dicc["Uguisudani"], dicc["Ueno"], {'color':'green', 'weight':1.1}),
                 (dicc["Ueno"], dicc["Okachimachi"], {'color':'green', 'weight':0.6}),
                 (dicc["Okachimachi"], dicc["Yamanote Akihabara"], {'color':'green', 'weight':1.0}),
                 (dicc["Yamanote Akihabara"], dicc["Akihabara"], {'color':'grey', 'weight':0.0}),
                 (dicc["Yamanote Akihabara"], dicc["Kanda"], {'color':'green', 'weight':0.7}),
                 (dicc["Kanda"], dicc["Yamanote Tokyo"], {'color':'green', 'weight':1.3}),
                 (dicc["Yamanote Tokyo"], dicc["Tokyo"], {'color':'grey', 'weight':0.0}),
                 (dicc["Yamanote Tokyo"], dicc["Yurakucho"], {'color':'green', 'weight':0.8}),
                 (dicc["Yurakucho"], dicc["Shimbashi"], {'color':'green', 'weight':1.1}),
                 (dicc["Shimbashi"], dicc["Hamamatsucho"], {'color':'green', 'weight':1.2}),
                 (dicc["Hamamatsucho"], dicc["Tamachi"], {'color':'green', 'weight':1.5}),
                 (dicc["Tamachi"], dicc["Shinagawa"], {'color':'green', 'weight':2.2}), 
                 (dicc["Shinagawa"], dicc["Osaki"], {'color':'green', 'weight':2.0}),
                 (dicc["Osaki"], dicc["Gotanda"], {'color':'green', 'weight':0.9}),
                 (dicc["Gotanda"], dicc["Meguro"], {'color':'green', 'weight':1.2}),
                 (dicc["Meguro"], dicc["Ebisu"], {'color':'green', 'weight':1.5}),
                 (dicc["Ebisu"], dicc["Shibuya"], {'color':'green', 'weight':1.6}),
                 (dicc["Shibuya"], dicc["Harajuku"], {'color':'green', 'weight':1.2}),
                 (dicc["Harajuku"], dicc["Yamanote Yoyogi"], {'color':'green', 'weight':1.5}),
                 (dicc["Yamanote Yoyogi"], dicc["Yoyogi"], {'color':'grey', 'weight':0.0}),
                 (dicc["Yamanote Yoyogi"], dicc["Yamanote Shinjuku"], {'color':'green', 'weight':0.7}),
                 (dicc["Yamanote Shinjuku"], dicc["Shinjuku"], {'color':'grey', 'weight':0.0}),
                 (dicc["Shinjuku"], dicc["Chuo Shinjuku"], {'color':'grey', 'weight':0.0}),
                 (dicc["Chuo Shinjuku"], dicc["Chuo Ochanomizu"], {'color':'red', 'weight':7.7}),
                 (dicc["Chuo Ochanomizu"], dicc["Ochanomizu"], {'color':'grey', 'weight':0.0}),
                 (dicc["Chuo Ochanomizu"], dicc["Chuo Tokyo"], {'color':'red', 'weight':2.6}),
                 (dicc["Chuo Tokyo"], dicc["Tokyo"], {'color':'grey', 'weight':0.0}),
                 (dicc["Shinjuku"], dicc["Sobu Shinjuku"], {'color':'grey', 'weight':0.0}),
                 (dicc["Sobu Shinjuku"], dicc["Sobu Yoyogi"], {'color':'yellow', 'weight':0.7}),
                 (dicc["Sobu Yoyogi"], dicc["Yoyogi"], {'color':'grey', 'weight':0.0}),
                 (dicc["Sobu Yoyogi"], dicc["Sendagaya"], {'color':'yellow', 'weight':1.0}),
                 (dicc["Sendagaya"], dicc["Shinanomachi"], {'color':'yellow', 'weight':0.7}),
                 (dicc["Shinanomachi"], dicc["Yotsuya"], {'color':'yellow', 'weight':1.3}),
                 (dicc["Yotsuya"], dicc["Ichigaya"], {'color':'yellow', 'weight':0.8}),
                 (dicc["Ichigaya"], dicc["Iidabashi"], {'color':'yellow', 'weight':1.5}),
                 (dicc["Iidabashi"], dicc["Suidobashi"], {'color':'yellow', 'weight':0.9}),
                 (dicc["Suidobashi"], dicc["Sobu Ochanomizu"], {'color':'yellow', 'weight':0.8}),
                 (dicc["Sobu Ochanomizu"], dicc["Ochanomizu"], {'color':'grey', 'weight':0.0}),
                 (dicc["Sobu Ochanomizu"], dicc["Sobu Akihabara"], {'color':'yellow', 'weight':0.9}),
                 (dicc["Sobu Akihabara"], dicc["Akihabara"], {'color':'grey', 'weight':0.0}),
                 (dicc["Yamanote Yoyogi"], dicc["Sobu Yoyogi"], {'color' :'grey', 'weight':0.2}),
                 (dicc["Yamanote Shinjuku"], dicc["Chuo Shinjuku"], {'color':'grey', 'weight':0.2}),
                 (dicc["Yamanote Akihabara"], dicc["Sobu Akihabara"], {'color':'grey', 'weight':0.2})
                 ])

#Heurisitica (lista h tal que h[i] = heuristica del dicc[nodo] = i)
#TODO
#Añadir las heuristicas de los nodos extra!
#Leer la fila correspondiente del csv



#Diccionario ejemplo
#dicc = { 'La Coruña': 0, 'Madrid': 1,'Barcelona': 2, 'Valencia': 3, 'Cádiz': 4}
#Inverso de dicc 
#diccInv = {v: k for k, v in dicc.items()}

#Grafo ejemplo
#G = Graph()
#G.add_weighted_edges_from([(dicc['La Coruña'], dicc['Madrid'], 5),
#                           (dicc['Madrid'], dicc['Barcelona'], 2), 
#                           (dicc['Madrid'], dicc['Valencia'], 1), 
#                           (dicc['Barcelona'], dicc['Cádiz'], 2), 
                           #(dicc['Barcelona'], dicc['Valencia'], -3),
#                           (dicc['Valencia'], dicc['Cádiz'], 4)])

#Heuristica ejemplo
h = [7, 5, 1, 2, 0, 2, 3, 4, 5 , 5 , 5, 4, 7, 4, 7, 4, 2, 9, 2, 8, 2, 4, 1, 4, 2, 5, 8, 3, 1,2, 6, 9, 3, 6, 8, 2, 2, 3, 5, 
     2,4, 5,3, 2,4, 3, 2]


#Pasar G y h como parametros?
def algoritmoA_Estrella(origenNombre, destinoNombre) :
    origen = dicc[origenNombre]
    destino = dicc[destinoNombre]
    #PriorityQueue de duplas (f , nombre)
    listaAbierta = []
    #Lista
    listaCerrada = []
    
    #Listas auxiliares f, g y puntero, inicializadas con -1
    #no se usaran todas sus posiciones, tendran "huecos"
    f = []
    g = []
    puntero = []
    for i in range(0, G.number_of_nodes()) :
        f.append(-1) 
        g.append(-1)
        puntero.append(-1)
        
    #Inicializar el nodo origen
    g[origen] = 0
    f[origen] = g[origen] + h[origen]
    heappush(listaAbierta, (f[origen], origen))

    hemosLlegado = False 
    
    while (not hemosLlegado) :

        nodoPrometedor = heappop(listaAbierta)[1]
        listaCerrada.append(nodoPrometedor)
     
        if (nodoPrometedor == destino) :
            hemosLlegado = True
        else :
            for nodoSiguiente in list(G.adj[nodoPrometedor]):
                #Se calculan f y g provisionales pero todavia no se guardan
                g_nodoSiguiente = g[nodoPrometedor] + G.edges[nodoPrometedor, nodoSiguiente]['weight']
                f_nodoSiguiente = g_nodoSiguiente + h[nodoSiguiente] 
                G.remove_edge(nodoPrometedor, nodoSiguiente)
                
                #Si hay un elemento con nodoSiguiente en listaAbierta
                #(aunque no necesariamente con la f que se acaba de calcular)
                if (estaEn(listaAbierta, nodoSiguiente, 1) or (nodoSiguiente in listaCerrada)
                    and f_nodoSiguiente < f[nodoSiguiente]) :
                    #Si mejora el camino, se guardan los nuevos f y g, 
                    #se actualizan el puntero y f en la listaAbierta
                    guardarValores(nodoSiguiente, g, g_nodoSiguiente, f, f_nodoSiguiente, puntero, nodoPrometedor)
                    actualizarValor(listaAbierta, nodoSiguiente, f[nodoSiguiente])
                #if (nodoSiguiente in listaCerrada) :
                    #TODO??
                if (not estaEn(listaAbierta, nodoSiguiente, 1) and (nodoSiguiente not in listaCerrada)) :
                    #Si no se habia explorado el nodo, se guardan f, g, puntero 
                    #y se introduce en la listaAbierta
                    guardarValores(nodoSiguiente, g, g_nodoSiguiente, f, f_nodoSiguiente, puntero, nodoPrometedor)
                    heappush(listaAbierta, (f[nodoSiguiente], nodoSiguiente))
                    
    if (hemosLlegado) :
        return calcularRuta(puntero, origen, destino)
    else :
        print('Error')
                   

def guardarValores(nodo, g, valor_g, f, valor_f, puntero, nodoAnterior) :
    g[nodo] = valor_g
    f[nodo] = valor_f
    puntero[nodo] = nodoAnterior
    
#Mira si hay una dupla en la lista de duplas cuya coordenada n-esima sea elem
def estaEn(listaDuplas, elem, n):
    return len([dupla[n] for dupla in listaDuplas if dupla[n] == elem]) > 0
            
#Actualiza un valor en un heap
def actualizarValor(heap, nodo, nuevoValor) :
    #Busca y elimina el antiguo
    elemento = [tupla for tupla in heap if tupla[1] == nodo][0]
    heap.remove(elemento)
    #Reconvierte en heap
    heapify(heap)
    #Añade el elemento con el nuevo valor
    heappush(heap, (nuevoValor, nodo))
    
#Devuelve una lista con los nombres de los nodos del camino optimo en orden 
def calcularRuta(puntero, origen, destino) :
    camino = [diccInv[destino]]
    anterior = puntero[destino]
    while (anterior != origen) :
        camino.append(diccInv[anterior])
        anterior = puntero[anterior]
    camino.append(diccInv[origen])
    camino.reverse()
    return camino
          
 
print('\nBeep-Boop-Bop...\nBeep-Boop-Bop...\n')
print(algoritmoA_Estrella('Ueno', 'Osaki'))
#print(algoritmoA_Estrella('La Coruña', 'Cádiz'))
    
    
    
    
