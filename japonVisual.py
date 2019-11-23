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
#TODO

#Grafo ()
#TODO

#Heurisitica (lista h tal que h[i] = heuristica del dicc[nodo] = i)
#TODO



#Diccionario ejemplo
dicc = { 'La Coruña': 0, 'Madrid': 1,'Barcelona': 2, 'Valencia': 3, 'Cádiz': 4}
#Inverso de dicc 
diccInv = {v: k for k, v in dicc.items()}

#Grafo ejemplo
G = Graph()
G.add_weighted_edges_from([(dicc['La Coruña'], dicc['Madrid'], 5),
                           (dicc['Madrid'], dicc['Barcelona'], 2), 
                           (dicc['Madrid'], dicc['Valencia'], 1), 
                           (dicc['Barcelona'], dicc['Cádiz'], 2), 
                           #(dicc['Barcelona'], dicc['Valencia'], -3),
                           (dicc['Valencia'], dicc['Cádiz'], 4)])

#Heuristica ejemplo
h = [7, 5, 1, 2, 0]


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
print(algoritmoA_Estrella('La Coruña', 'Cádiz'))
    
    
    
    