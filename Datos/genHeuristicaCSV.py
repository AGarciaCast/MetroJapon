# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 00:15:40 2019

@author: Alejandro
"""
import csv

lista=[]

"""
/**************************************************
* Title: Coordinate Reference Systems
* Author: spk578
* Date: 2017
* Availability: https://community.esri.com/groups/coordinate-reference-systems/blog/2017/10/05/haversine-formula
***************************************************/
"""
def haversine(lon1, lat1, lon2, lat2):
    R = 6371000  # radius of Earth in meters
    phi_1 = math.radians(lat1)
    phi_2 = math.radians(lat2)

    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2.0) ** 2 + math.cos(phi_1) * math.cos(phi_2) * math.sin(delta_lambda / 2.0) ** 2
    
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    meters = R * c  # output distance in meters
    km = meters / 1000.0  # output distance in kilometers
    return round(km, 2)

coordenadasEstaciones=[
{'name':'Shinagawa','lat':35.628557,'lon':139.73877},
{'name':'Osaki','lat':35.619863,'lon':139.728195},
{'name':'Gotanda','lat':35.626180,'lon':139.723614},
{'name':'Meguro','lat':35.634128,'lon':139.715833},
{'name':'Ebisu','lat':35.646714,'lon':139.710067},
{'name':'Shibuya','lat':35.658077,'lon':139.701636},
{'name':'Harajuku','lat':35.670255,'lon':139.702676},
{'name':'Yoyogi','lat':35.683077,'lon':139.702066},
{'name':'Shinjuku','lat':35.689781,'lon':139.700389},
{'name':'Shin-Okubo','lat':35.701268,'lon':139.700228},
{'name':'Takadanobaba','lat':35.712624,'lon':139.703603},
{'name':'Mejiro','lat':35.721179,'lon':139.706566},
{'name':'Ikebukuro','lat':35.729511,'lon':139.710911},
{'name':'Otsuka','lat':35.731691,'lon':139.728432},
{'name':'Sugamo','lat':35.733428,'lon':139.739283},
{'name':'Komagome','lat':35.736576,'lon':139.747013},
{'name':'Tabata','lat':35.738186,'lon':139.760823},
{'name':'Nishi-Nippori','lat':35.732025,'lon':139.766888},
{'name':'Nippori','lat':35.728166,'lon':139.770643},
{'name':'Uguisudani','lat':35.721461,'lon':139.778006},
{'name':'Ueno','lat':35.714189,'lon':139.777402},
{'name':'Okachimachi','lat':35.707551,'lon':139.774861},
{'name':'Akihabara','lat':35.698401,'lon':139.773067},
{'name':'Kanda','lat':35.691827,'lon':139.770927},
{'name':'Tokyo','lat':35.681246,'lon':139.76711},
{'name':'Yurakucho','lat':35.674926,'lon':139.762816},
{'name':'Shimbashi','lat':35.666387,'lon':139.758346},
{'name':'Hamamatsucho','lat':35.655391,'lon':139.757122},
{'name':'Tamachi','lat':35.645752,'lon':139.747575},
{'name':'Ochanomizu','lat':35.699394,'lon':139.765258},
{'name':'Suidobashi','lat':35.702073,'lon':139.753503},
{'name':'Iidabashi','lat':35.702087,'lon':139.745034},
{'name':'Ichigaya','lat':35.691021,'lon':139.735575},
{'name':'Yotsuya','lat':35.686154,'lon':139.730217},
{'name':'Shinanomachi','lat':35.680075,'lon':139.720311},
{'name':'Sendagaya','lat':35.681215,'lon':139.711285}
]




with open('heuristicaMetroJapon.csv', 'wb') as japon_file:
    japon_writer = csv.writer(japon_file, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
    japon_writer.writerow([estacion['name'] for estacion in coordenadasEstaciones])
    for estacionOrigen in coordenadasEstaciones:
        for estaconDestino in coordenadasEstaciones:
            lista.append(haversine(estacionOrigen['lon'],estacionOrigen['lat'],estaconDestino['lon'],estaconDestino['lat']))
        japon_writer.writerow(lista)
        lista =[]
    